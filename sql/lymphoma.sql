SELECT
	cell.cell_id,
	pert.pert_id,
	pert.pert_iname,
	pert.dc_id
FROM
	cell
JOIN
	signature sig ON sig.cell_id = cell.cell_id
JOIN
	perturbagen pert ON pert.pert_id = sig.pert_id
WHERE
	cell.cell_histology ~* 'lymphoma'
	AND pert.dc_id IS NOT NULL
ORDER BY
	pert.pert_iname
	;

