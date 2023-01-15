import pandas as pd
import regex


def get_type(gene_data, col, conditions):
    re_type_all = []
    seqs = pd.Series(gene_data['seq'])
    for seq in seqs:
        re_type = [False] * len(col)
        for item in range(len(conditions)):
            if regex.search(conditions[item], str(seq)) is not None:
                re_type[item] = True
        re_type_all.append(re_type)
    re_type_all = pd.DataFrame(re_type_all, columns=col)
    return pd.concat([gene_data, re_type_all], axis=1)
