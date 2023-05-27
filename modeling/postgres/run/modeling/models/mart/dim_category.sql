
  
    

  create  table "personal_finance"."public_mart"."dim_category__dbt_tmp"
  
  
    as
  
  (
    WITH src AS (

    SELECT DISTINCT category
    FROM "personal_finance"."public_staging"."stg_transactions"

), 

numbered AS (
    SELECT 
        row_number() OVER (ORDER BY category) AS category_id,
        category
    FROM src
)

SELECT 
    category_id,
    category
FROM numbered
  );
  