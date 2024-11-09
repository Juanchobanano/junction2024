SELECT production_date, SUM(batch_weight) AS total_weight
FROM production_data
GROUP BY production_date
ORDER BY production_date;