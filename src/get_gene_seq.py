from Bio import SeqIO
import pandas as pd


def get_gene_seq(geneseq, orf):
    if orf is True:
        all = []
        for seq_record in SeqIO.parse(geneseq, 'fasta'):
            all.append([seq_record.id, str(seq_record.seq).upper()])
        gene_seq = pd.DataFrame(all, columns=['id', 'seq'])
    else:
        if geneseq == 'gene_seq.pkl':
            gene_seq = pd.read_pickle(geneseq)
        else:
            gene_seq = pd.read_csv(geneseq)
    return gene_seq
