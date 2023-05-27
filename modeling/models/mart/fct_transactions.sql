SELECT 
    TO_DATE(transaction_date, 'DD-MM-YYYY') AS transaction_date,
    details::TEXT,
    a.account_id::INTEGER,
    c.category_id::INTEGER,
    s.subcategory_id::INTEGER,
    notes::TEXT,
    debit::DECIMAL,
    credit::DECIMAL,
    balance::DECIMAL,
    original_description::TEXT
FROM {{ ref('stg_transactions') }} t
LEFT JOIN {{ ref('dim_account') }} a
ON t.account = a.account
LEFT JOIN {{ ref('dim_category') }} c
ON t.category = c.category
LEFT JOIN {{ ref('dim_subcategory') }} s
ON t.subcategory = s.subcategory
