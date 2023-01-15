import pandas as pd
import pysam

# gff = '02_开发/STOP RNA/命令行/测试文件/fly_genomic.gff'
# fna = '02_开发/STOP RNA/命令行/测试文件/fly_genome.fna'


def get_gene_data(genome, gff):
    temp_file = open(gff, 'r')
    skip_row = 0
    for i in range(10):
        if temp_file.readline().startswith('#'):
            continue
        else:
            skip_row = i
            break
    temp_file.close()
    del temp_file
    gene_data_more = pd.read_csv(
        gff, sep="\t", header=None, low_memory=False, skiprows=skip_row, usecols=[0, 3, 4, 8])
    gene_data_more.dropna(inplace=True)
    gene_data_more = gene_data_more.rename(
        columns={0: 'chr', 3: 'start', 4: 'end', 8: 'infor'})
    gene_data_temp = pd.Series(gene_data_more['infor'])
    gene_infor = []
    for item in gene_data_temp:
        infor = [None, None, None]
        for i in item.split(';'):
            if 'ID=' in i:
                if 'ID=exon-' in i:
                    infor[0] = i.split('ID=exon-')[1].split('-')[0]
                    infor[1] = i.split('ID=exon-')[1].split('-')[1]
                else:
                    infor[0] = i
            elif 'gene=' in i:
                infor[2] = i.split('gene=')[1]
        gene_infor.append(infor)
    gene_data_more.drop('infor', axis=1, inplace=True)
    gene_infor = pd.DataFrame(gene_infor, columns=['id', 'exon', 'gene_name'])
    gene_data_more.reset_index(drop=True, inplace=True)
    gene_data_need = pd.concat([gene_data_more, gene_infor], axis=1)
    del gene_data_temp, gene_infor, gene_data_more
    gene_data_need.dropna(inplace=True)
    gene_data_need = gene_data_need[gene_data_need['id'].str.contains(
        'NM', na=False)]
    gene_data_need = gene_data_need[~gene_data_need['chr'].str.contains(
        'NC_000023|NC_000024|12920|NW|NT', na=False)]
    gene_data_need = gene_data_need.reset_index(drop=True)
    fa = pysam.FastaFile(genome)
    seq = []
    for i in range(len(gene_data_need)):
        seq.append(fa.fetch(gene_data_need.at[i, 'chr'],
                            start=gene_data_need.at[i, 'start'] - 1,
                            end=gene_data_need.at[i, 'end']).upper())
    seq = pd.DataFrame(seq, columns=['seq'])
    gene_data = pd.concat([gene_data_need, seq], axis=1)
    return gene_data


# if __name__ == "__main__":
#     get_gene_data(genome, gff)
