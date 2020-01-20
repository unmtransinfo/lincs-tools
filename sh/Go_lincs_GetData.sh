#!/bin/bash
###

cwd="$(pwd)"
DATADIR="${cwd}/data"

#
cmap_query.py listGenes_landmark --o $DATADIR/clue_genes_L1000.tsv
#
cmap_query.py listDrugs --o $DATADIR/clue_drugs.tsv
#
cmap_query.py listCells --o $DATADIR/clue_cells.tsv
pandas_utils.py colvalcounts --coltags primary_disease \
	--i $DATADIR/clue_cells.tsv
pandas_utils.py selectcols --coltags cell_iname \
	--i $DATADIR/clue_cells.tsv \
	|sed -e '1d' |sort -u >$DATADIR/clue_cells.cell_id
#
###
# lymphoma
pandas_utils.py searchrows --coltags primary_disease --search_qrys lymphoma \
	--i $DATADIR/clue_cells.tsv \
	--o $DATADIR/clue_cells-lymphoma.tsv
pandas_utils.py selectcols --coltags cell_iname \
	--i $DATADIR/clue_cells-lymphoma.tsv \
	|sed -e '1d' |sort -u >$DATADIR/clue_cells-lymphoma.cell_id
#
rm -f $DATADIR/clue_cells-lymphoma_sig.tsv
n_cells=$(cat $DATADIR/clue_cells-lymphoma.cell_id |wc -l)
i=0
while [ $i -lt $n_cells ]; do
	i=$(($i + 1))
	cell_id=$(cat $DATADIR/clue_cells-lymphoma.cell_id |sed "${i}q;d")
	printf "%d/%d. cell_id: \"%s\"\n" "$i" "$n_cells" "$cell_id"
	if [ $i -eq 1 ]; then
		cmap_query.py getSignatures --clue_where "{\"cell_id\":\"${cell_id}\"}" >$DATADIR/clue_cells-lymphoma_sig.tsv
	else
		cmap_query.py getSignatures --clue_where "{\"cell_id\":\"${cell_id}\"}" |sed -e '1d' >>$DATADIR/clue_cells-lymphoma_sig.tsv
	fi
done
#
