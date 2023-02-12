# import pandas as pd
import regex


# def get_type(gene_data, col, conditions):
#     re_type_all = []
#     seqs = pd.Series(gene_data['seq'])
#     for seq in seqs:
#         re_type = [False] * len(col)
#         for item in range(len(conditions)):
#             if regex.search(conditions[item], str(seq)) is not None:
#                 re_type[item] = True
#         re_type_all.append(re_type)
#     re_type_all = pd.DataFrame(re_type_all, columns=col)
#     return pd.concat([gene_data, re_type_all], axis=1)


def for_pat_exist(gene_data, cond):
    def get_type(x):
        codon_num = 0
        for codon in ['CAA', 'CAG', 'CGA']:
            if codon in cond.pattern:
                codon_num = cond.pattern.find(codon)
                continue
            else:
                break
        for pos_item in regex.finditer(cond, x, overlapped=True):
            # codons = ['CAA','CAG','CGA']
            # min_pos = [pos_item.group().find('CAA'), pos_item.group().find('CAG'),pos_item.group().find('CGA')].index(min(pos_item.group().find('CAA'), pos_item.group().find('CAG'),pos_item.group().find('CGA')))
            # codon_item = codons[min_pos]
            if (pos_item.span()[0] + codon_num) % 3 == 0:
                return str(pos_item.span())[1:-1]
        return 0

    gene_data[cond.pattern] = gene_data.seq.map(get_type)


def re_pat_exist(gene_data, cond):
    def get_type(x):
        cond_num = cond.pattern.rfind('TGG')
        cond_len = len(cond.pattern)
        for pos_item in regex.finditer(cond, x, overlapped=True):
            if (pos_item.span()[1] + 1 + cond_len - cond_num) % 3 == 0:
                return str(pos_item.span())[1:-1]
        return 0

    gene_data[cond.pattern] = gene_data.seq.map(get_type)


def get_pos(gene_data, conditions):
    for condition in conditions:
        if 'TGG' not in condition.pattern:
            for_pat_exist(gene_data, cond=condition)
        else:
            re_pat_exist(gene_data, cond=condition)

        # if 'TGG' not in condition.pattern:
        #     for_pat_exist(gene_data, cond= condition)
        # else:
        #     re_pat_exist(gene_data, cond= condition)
