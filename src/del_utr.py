def combine_exon(gene_data):
    gene_data_temp = gene_data.copy()
    gene_data_temp['seq'] = gene_data_temp.groupby('id')['seq'].transform('sum')
    gene_data_temp = gene_data_temp.drop_duplicates('id', keep='first').reset_index(
        drop=True
    )
    gene_data_temp['pos_seq_pos'] = gene_data_temp.seq.map(
        lambda x: len(x.split('ATG')[0])
    )
    gene_data_temp['seq'] = gene_data_temp.seq.map(
        lambda x: 'ATG' + ''.join(x.split('ATG')[1:])
    )
    gene_data_temp.drop('id', axis=1, inplace=True)
    return gene_data_temp
