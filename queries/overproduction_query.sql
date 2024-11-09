SELECT production_date, SUM(batch_weight) AS total_weight
FROM production_data
GROUP BY production_date
HAVING total_weight > 10000
ORDER BY production_date;
