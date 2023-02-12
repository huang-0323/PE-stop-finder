def exon_create(gene_data):
    gene_data_temp = gene_data.copy()
    all_line = gene_data_temp.exon == '1'
    for i in range(int(max(gene_data_temp.exon))):
        gene_data_temp.loc[all_line, 'seq'] = gene_data_temp[all_line].seq.map(
            lambda x: 'ATG' + ''.join(x.split('ATG')[1:])
        )
        if any(gene_data_temp[all_line].seq == 'ATG') == True:
            all_line = (
                gene_data_temp.id.isin(
                    gene_data_temp[all_line & (gene_data_temp.seq == 'ATG')].id.tolist()
                )
            ) & (gene_data_temp.exon == str(i + 1))
        else:
            break
    gene_data_temp = gene_data_temp[~gene_data_temp.seq.isin(['ATG'])]

    def del_bytes(df):
        temp_list = []
        for_num = 0
        for line in df.seq:
            line = line[for_num:]
            if len(line) % 3 == 0:
                for_num = 0
            else:
                last = len(line) % 3
                line = line[:-last]
                for_num = 3 - last
            temp_list.append(line)
        df.loc[:, 'seq'] = temp_list
        return df

    return (
        gene_data_temp.groupby('id', group_keys=False)
        .apply(del_bytes)
        .reset_index(drop=True)
    )
