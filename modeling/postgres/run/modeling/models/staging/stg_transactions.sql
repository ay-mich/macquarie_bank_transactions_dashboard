
  
    

  create  table "personal_finance"."public_staging"."stg_transactions__dbt_tmp"
  
  
    as
  
  (
    WITH src AS (

    SELECT *
    FROM "personal_finance"."staging"."raw_transactions"

)

SELECT 
    "Transaction Date" AS transaction_date,
    "Details" AS details,
    "Account" AS account,
    "Category" AS category,
    "Subcategory" AS subcategory,
    "Notes" AS notes,
    "Debit" AS debit,
    "Credit" AS credit,
    "Balance" AS balance,
    "Original Description" AS original_description
FROM src
  );
  