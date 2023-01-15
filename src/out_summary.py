import pandas as pd


def out_summary(out, gene_infor, genome, gff, region, motif, cols):
    gene_infor.to_csv(f'{out}.stop.summary.csv')
    exon_coverage, id_coverage, gene_coverage = [], [], []
    for col in cols:
        exon_coverage.append(
            len(gene_infor[gene_infor[col] == True])
            / len(gene_infor)
        )
        id_coverage.append(
            len(gene_infor[gene_infor[col] == True].id.value_counts())
            / len(gene_infor.id.value_counts())
        )
        gene_coverage.append(
            len(gene_infor[gene_infor[col] == True].gene_name.value_counts())
            / len(gene_infor.gene_name.value_counts())
        )
    gene_coverage_infor = pd.DataFrame(
        [exon_coverage, id_coverage, gene_coverage],
        index=['exon', 'id', 'gene'],
        columns=cols,
    )
    gene_coverage_infor.to_csv(f'{out}.coverage.summary.csv')
    return 1
