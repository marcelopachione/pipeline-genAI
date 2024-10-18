{{ config(MATERIALIZED='view') }}

SELECT
    *
FROM
    {{ source('vendas_source', 'vendas') }}