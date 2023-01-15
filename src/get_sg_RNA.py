import pandas as pd
import regex


def out_design(gene_seq, condition):
    all = []
    for item_index in range(len(gene_seq)):
        all.append(
            [
                gene_seq.at[item_index, 'chr'],
                gene_seq.at[item_index, 'start'],
                gene_seq.at[item_index, 'end'],
                gene_seq.at[item_index, 'id'],
                gene_seq.at[item_index, 'exon'],
                gene_seq.at[item_index, 'gene_name'],
                ','.join(
                    regex.findall(
                        condition, gene_seq.at[item_index, 'seq'], overlapped=True
                    )
                ),
            ]
        )
    gene_sg_seq = pd.DataFrame(
        all, columns=['chr', 'start', 'end', 'id', 'exon', 'gene_name', 'sg_RNA']
    )
    return gene_sg_seq
