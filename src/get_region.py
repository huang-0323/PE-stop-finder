def get_region(gene_data, region):
    region = ''.join(region.split(' '))
    region = region.replace(',', '|')
    gene_data = gene_data[gene_data['chr'].str.contains(region)]
    return gene_data


# a = pd.read_pickle('02_开发/STOP RNA/命令行/tset.pkl')
# get_region(a, 'NC_004354.4')
