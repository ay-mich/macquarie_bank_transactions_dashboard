WITH src AS (

    SELECT DISTINCT account
    FROM {{ ref('stg_transactions') }}

), 

numbered AS (
    SELECT 
        row_number() OVER (ORDER BY account) AS account_id,
        account
    FROM src
)

SELECT 
    account_id::INTEGER,
    account::TEXT
FROM numbered
