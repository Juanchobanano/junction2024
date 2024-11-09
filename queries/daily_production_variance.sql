SELECT production_date,
       VARIANCE(batch_weight) AS batch_weight_variance
FROM production_data
GROUP BY production_date
ORDER BY production_date;
