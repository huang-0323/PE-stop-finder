import pandas as pd


def out_orf_summary(out, gene_data, condition):
    cols = [i.pattern for i in condition]
    exon_coverage = []
    exist = [False] * len(gene_data)
    for col in range(len(cols), 0, -1):
        exon_coverage.append(
            len(gene_data[gene_data.iloc[:, -col] != 0]) / len(gene_data)
        )
        exist = exist | (gene_data.iloc[:, -col] != 0)
    gene_data = pd.concat([gene_data, pd.DataFrame({'exist': exist})], axis=1)
    exon_coverage.append(list(exist).count(True) / len(gene_data))
    cols.append('exist')
    gene_coverage_infor = pd.DataFrame([exon_coverage], columns=cols, index=['orf'])
    gene_coverage_infor.to_csv(f'{out}_orf_coverage_summary.csv')
    return 1


def out_gene_summary(out, gene_exon_data, gene_id_data, condition):
    exon_coverage, id_coverage, gene_coverage = [], [], []
    cols = [i.pattern for i in condition]
    exist_exon, exist_id = [False] * len(gene_exon_data), [False] * len(gene_id_data)
    for col in range(len(cols), 0, -1):
        exon_coverage.append(
            len(gene_exon_data[gene_exon_data.iloc[:, -col] != 0]) / 736617
        )
        exist_exon = exist_exon | (gene_exon_data.iloc[:, -col] != 0)
        id_coverage.append(
            len(gene_id_data[gene_id_data.iloc[:, -col] != 0]) / len(gene_id_data)
        )
        gene_coverage.append(
            len(gene_id_data[gene_id_data.iloc[:, -col] != 0].gene_name.value_counts())
            / len(gene_id_data.gene_name.value_counts())
        )
        exist_id = exist_id | (gene_id_data.iloc[:, -col] != 0)
    exon_coverage.append(list(exist_exon).count(True) / 736617)
    id_coverage.append(list(exist_id).count(True) / len(gene_id_data))
    gene_exon = pd.concat([gene_exon_data, pd.DataFrame({'exist': exist_exon})], axis=1)
    gene_exon.to_csv(f'{out}_exon_stop_summary.csv')
    gene_id = pd.concat([gene_id_data, pd.DataFrame({'exist': exist_id})], axis=1)
    gene_id.to_csv(f'{out}_id_stop_summary.csv')
    gene_coverage.append(
        len(gene_id[gene_id['exist'] != 0].gene_name.value_counts())
        / len(gene_id.gene_name.value_counts())
    )
    cols.append('exist')
    gene_coverage_infor = pd.DataFrame(
        [exon_coverage, id_coverage, gene_coverage],
        index=['exon_coverage', 'id_coverage', 'gene_coverage'],
        columns=cols,
    )
    gene_coverage_infor.to_csv(f'{out}_id_coverage_summary.csv')
    return 1
