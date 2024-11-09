SELECT DATE_TRUNC('month', production_date) AS production_month,
       AVG(batch_weight) AS avg_batch_weight
FROM production_data
GROUP BY production_month
ORDER BY production_month;
