SELECT
	ROUND(CAST(percentile_disc(0.01) WITHIN GROUP (ORDER BY zscore) AS NUMERIC), 3) zscore_pctile_01,
	ROUND(CAST(percentile_disc(0.05) WITHIN GROUP (ORDER BY zscore) AS NUMERIC), 3) zscore_pctile_05,
	ROUND(CAST(percentile_disc(0.1) WITHIN GROUP (ORDER BY zscore) AS NUMERIC), 3) zscore_pctile_10,
	ROUND(CAST(percentile_disc(0.25) WITHIN GROUP (ORDER BY zscore) AS NUMERIC), 3) zscore_pctile_25,
	ROUND(CAST(percentile_disc(0.5) WITHIN GROUP (ORDER BY zscore) AS NUMERIC), 3) zscore_pctile_50,
	ROUND(CAST(percentile_disc(0.75) WITHIN GROUP (ORDER BY zscore) AS NUMERIC), 3) zscore_pctile_75,
	ROUND(CAST(percentile_disc(0.9) WITHIN GROUP (ORDER BY zscore) AS NUMERIC), 3) zscore_pctile_90,
	ROUND(CAST(percentile_disc(0.95) WITHIN GROUP (ORDER BY zscore) AS NUMERIC), 3) zscore_pctile_95,
	ROUND(CAST(percentile_disc(0.99) WITHIN GROUP (ORDER BY zscore) AS NUMERIC), 3) zscore_pctile_99
FROM
	level5_lm
	;
--
