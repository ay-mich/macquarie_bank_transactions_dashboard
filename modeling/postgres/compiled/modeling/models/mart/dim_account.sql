WITH src AS (

    SELECT DISTINCT account
    FROM "personal_finance"."public_staging"."stg_transactions"

), 

numbered AS (
    SELECT 
        row_number() OVER (ORDER BY account) AS account_id,
        account
    FROM src
)

SELECT 
    account_id,
    account
FROM numbered