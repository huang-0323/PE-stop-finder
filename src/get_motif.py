import regex

# motif = '02_开发/STOP RNA/命令行/测试文件/motif1.txt'


def get_condition(motif):
    base_dict = [
        ['R', '[AG]'],
        ['Y', '[CT]'],
        ['S', '[GC]'],
        ['W', '[AT]'],
        ['K', '[GT]'],
        ['M', '[AC]'],
        ['B', '[CGT]'],
        ['D', '[AGT]'],
        ['H', '[ACT]'],
        ['V', '[ACG]'],
        ['N', '[ACGT]'],
        ['(', '{'],
        [')', '}'],
    ]
    with open(motif, 'r') as f:
        f_in = f.read().upper().strip().splitlines()
    col = []
    for item in f_in:
        col.append(item.split('(')[0][:3] + '-' + item.split(')')[-1][-3:])
    conditions = []
    condition_all = ''
    for item in range(len(f_in)):
        for item_b in base_dict:
            f_in[item] = f_in[item].replace(item_b[0], item_b[1])
        conditions.append(regex.compile(f_in[item]))
        condition_all += f'{f_in[item]}|'
    condition_all = regex.compile(condition_all[:-1])
    return [col, f_in, condition_all]


# a = get_condition(motif)
