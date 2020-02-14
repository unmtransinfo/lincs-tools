SELECT
	ROUND(CAST(MIN(zscore) AS NUMERIC), 3) min_zscore,
	ROUND(CAST(MAX(zscore) AS NUMERIC), 3) max_zscore,
	ROUND(CAST(AVG(zscore) AS NUMERIC), 3) avg_zscore,
	ROUND(CAST(percentile_disc(0.5) WITHIN GROUP (ORDER BY zscore) AS NUMERIC), 3) med_zscore
FROM
	level5_lm
	;
--
