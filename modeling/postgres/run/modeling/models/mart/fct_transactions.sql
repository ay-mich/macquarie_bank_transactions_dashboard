
  
    

  create  table "personal_finance"."public_mart"."fct_transactions__dbt_tmp"
  
  
    as
  
  (
    SELECT 
    transaction_date,
    details,
    a.account_id,
    c.category_id,
    s.subcategory_id,
    notes,
    debit,
    credit,
    balance,
    original_description
FROM "personal_finance"."public_staging"."stg_transactions" t
LEFT JOIN "personal_finance"."public_mart"."dim_account" a
ON t.account = a.account
LEFT JOIN "personal_finance"."public_mart"."dim_category" c
ON t.category = c.category
LEFT JOIN "personal_finance"."public_mart"."dim_subcategory" s
ON t.subcategory = s.subcategory
  );
  