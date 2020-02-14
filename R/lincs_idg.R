library(readr)
library(data.table)

genes <- read_delim("data/lincs_genes_lm_sql_out.tsv", "\t")
setDT(genes)

idg <- read_delim("/home/data/IDG/idg-tools/data/tcrd_targets.tsv", "\t")
setDT(idg)

genes <- merge(genes, idg[, .(tcrdTargetId, tcrdProteinId, tcrdGeneSymbol, uniprotId, tcrdTargetName, tcrdTargetFamily, TDL)], by.x="pr_gene_symbol", by.y="tcrdGeneSymbol", all.x=T, all.y=F)

message(sprintf("LINCS Landmark genes mapped to IDG: %d", nrow(genes[!is.na(tcrdTargetId)])))

write_delim(genes, "data/lincs_genes_lm_idg.tsv", "\t")
