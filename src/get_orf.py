import pandas as pd
from Bio import SeqIO


def get_orf(genome):
    orf_id = []
    orf_seq = []
    for item in SeqIO.parse(genome, 'fasta'):
        orf_id.append(item.id.split(':')[1])
        orf_seq.append(str(item.seq).upper())

    orf_data = pd.DataFrame({'id': orf_id, 'seq': orf_seq}, columns=['id', 'seq'])
    orf_data.insert(2, 'len', orf_data['seq'].str.len())
    orf_data.insert(3, 'shortlen', orf_data['len'] < 23)
    return orf_data
