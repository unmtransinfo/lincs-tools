library(readr)
library(data.table)

perturbagens <- read_delim("data/perturbagens_dc_sql_out.tsv", "\t")
setDT(perturbagens)

dc_structs <- read_delim("data/drugcentral_structs_sql_out.tsv", "\t")
setDT(dc_structs)

perturbagens <- merge(perturbagens, dc_structs, by.x="dc_id", by.y="dc_struct_id", all.x=T, all.y=F)

pert_suspicious <- perturbagens[pert_iname != dc_name]

message(sprintf("Perturbagens in DrugCentral: %d", nrow(perturbagens[!is.na(dc_name)])))

write_delim(perturbagens, "data/perturbagens_dc_merged.tsv", "\t")
