# Macquarie Bank Transactions Dashboard

This project creates a transactions dashboard by loading your exported CSV from Macquarie bank into a PostgreSQL database, applying the Kimball dimensional data warehouse model using DBT, and displaying your transactions in Metabase dashboards for analysis.

## Project Overview

This project is designed for individuals who want to analyze their financial transactions in a systematic and intuitive manner. With the help of this tool, you can transform your raw banking transactions into insightful dashboards. This can be useful for personal budgeting, understanding spending habits, and general financial planning.

## Technologies Used

- PostgreSQL
- dbt
- Metabase
- Docker
- Python

## Installation

1. Install [Docker](https://docs.docker.com/get-docker/)
2. Clone this repository: `bash git clone <repo-url>`
3. Log in to your Macquarie bank account and download your transactions as a CSV file.
4. Move your transaction CSV file to the /import directory within the cloned repository.
5. With Docker running, open a terminal and navigate to the repository's root directory.
6. Run the command `bash docker-compose up --build`.

## What does docker-compose up --build do?

- Starts the Postgres database, Metabase server and DBT service.
- Finds your CSV file and loads it to the database staging schema.
- Runs DBT to take your staging file and create a Kimball dimensional data warehouse model.
- Loads Metabase where you can view a template that has taken your data and created a dashboard.

## What's next?

- Create further reports and dashboard in Metabase.
- To update, simply log into your Macquarie bank account again, export your transactions CSV, move it to the /import folder and run `bash docker-compose up --build` again.
- Your existing dashboards will be persisted.

## Login details:

Please note: The provided credentials are for example purposes only. Replace them with secure credentials in a production environment.

Logging into Metabase

- User: hi@email.com
- Pass: transactor1

Database connection details, should you want to log in using pgAdmin or other tools:

- Host: db
- Post: 5432
- User: transactor
- Pass: password
- Database: my_transactions

## Generating Fake Data

This project comes with a script that generates a CSV file with fake transactions data using the Faker library. This can be useful for testing purposes or for demoing the functionality of the dashboard without needing to use real transaction data.

The generated data includes the following fields for each transaction:

- Transaction Date
- Details
- Account
- Category
- Subcategory
- Notes
- Debit
- Credit
- Balance
- Original Description

Categories and subcategories are chosen randomly from a predefined list. If a transaction falls under the "Income" category, a credit amount is recorded; for all other categories, a debit amount is recorded.

### Using the Fake Data Generator

To generate fake data:

1. Navigate to the scripts directory in the terminal.
2. Run the Python script `python python generate_fake_data.py`.
3. The script will generate 2000 rows of data by default and output the results to a CSV file located at ../import/fake.csv.
4. If you want to change the number of rows generated or the output file location, modify the NUM_ROWS and OUTPUT_FILE_PATH constants at the top of the script.
5. This script is particularly helpful when you want to test the functionality of the system or when demonstrating the capabilities of the dashboard.

## Notes:

- The modeling server is kept up as it's useful to run `bash dbt run` manually sometimes

## Contributing

Contributions to this project are welcome! If you have a feature request, bug report, or proposal for improving the code or documentation, please open an issue to discuss it. If you wish to contribute code, please open a pull request.

## License

This project is licensed under the MIT License.
