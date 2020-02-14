SELECT DISTINCT
        pert_id,
        pert_iname,
        dc_id,
        canonical_smiles
FROM
        perturbagen
WHERE
        dc_id IS NOT NULL
ORDER BY
        dc_id
        ;