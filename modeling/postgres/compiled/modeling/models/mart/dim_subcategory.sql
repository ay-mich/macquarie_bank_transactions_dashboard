WITH src AS (

    SELECT DISTINCT subcategory
    FROM "personal_finance"."public_staging"."stg_transactions"

), 

numbered AS (
    SELECT 
        row_number() OVER (ORDER BY subcategory) AS subcategory_id,
        subcategory
    FROM src
)

SELECT 
    subcategory_id,
    subcategory
FROM numbered