SELECT DISTINCT
        *
FROM
        gene
WHERE
        pr_is_lm = 1
ORDER BY
        pr_gene_symbol
;