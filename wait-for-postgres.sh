#!/bin/sh

# This script waits for PostgreSQL to be ready before executing a given command.

# Exit the script as soon as a command fails.
set -e

# Ensure necessary environment variables are set
: "${DB_PASS:?Need to set DB_PASS}"
: "${DB_USER:?Need to set DB_USER}"
: "${DB_NAME:?Need to set DB_NAME}"

# Hostname for the PostgreSQL server
host="$1"
shift

# Command to run after PostgreSQL is ready
cmd="$@"

# Counter to keep track of how long we've been waiting
counter=0

# Wait for PostgreSQL to be ready
until PGPASSWORD=$DB_PASS psql -h "$host" -p 5432 -U "$DB_USER" -d "$DB_NAME" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
  counter=$((counter + 1))
  # Timeout after 60 seconds
  if [ $counter -gt 60 ]; then
    >&2 echo "Timeout waiting for Postgres to be available"
    exit 1
  fi
done

# PostgreSQL is up, execute the command
>&2 echo "Postgres is up - executing command"
exec $cmd
