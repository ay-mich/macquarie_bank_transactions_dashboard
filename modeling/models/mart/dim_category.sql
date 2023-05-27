WITH src AS (

    SELECT DISTINCT category
    FROM {{ ref('stg_transactions') }}

), 

numbered AS (
    SELECT 
        row_number() OVER (ORDER BY category) AS category_id,
        category
    FROM src
)

SELECT 
    category_id::INTEGER,
    category::TEXT
FROM numbered
