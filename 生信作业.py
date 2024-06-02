# author 莫森 time:2024/3/25
# def reverse_complement(sequence):
#     complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
#     reverse = sequence[::-1]
#     reverse_complement = ''.join([complement[base] for base in reverse])
#     return reverse_complement
#
# def find_orf(sequence):
#     start_codons = ['ATG']
#     stop_codons = ['TAA', 'TAG', 'TGA']
#     orfs = []
#
#     for frame in range(3):
#         for i in range(frame, len(sequence), 3):
#             codon = sequence[i:i+3]
#             if codon in start_codons:
#                 orf = ''
#                 for j in range(i, len(sequence), 3):
#                     codon = sequence[j:j+3]
#                     if codon in stop_codons:
#                         orfs.append(orf)
#                         break
#                     orf += codon
#
#     return orfs
#
# def predict_orf(dna_sequence):
#     forward_orfs = find_orf(dna_sequence)
#     reverse_sequence = reverse_complement(dna_sequence)
#     reverse_orfs = find_orf(reverse_sequence)
#
#     all_orfs = forward_orfs + reverse_orfs
#     return all_orfs
#
# # 示例DNA序列
# dna_sequence = 'AGTTTTGTCC'
#
# # 预测ORF
# orf_predictions = predict_orf(dna_sequence)
#
# # 打印结果
# for i, orf in enumerate(orf_predictions):
#     print(f'ORF {i+1}: {orf}')

# # 密码子表字典
codon_table = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGG': 'W',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}
def find_orf(dna_sequence):
    start_codon = list(codon_table.keys())
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []
    # 找到所有可能的起始密码子位置
    start_positions = [i for i in range(len(dna_sequence) - 2) if dna_sequence[i:i+3] in start_codon]
    if start_positions :
    # 对于每个起始密码子，找到对应的终止密码子位置
        for start_pos in start_positions:
            for i in range(start_pos + 3, len(dna_sequence) - 2, 3):
                codon = dna_sequence[i:i+3]
                if codon in stop_codons:
                    orf = dna_sequence[start_pos:i+3]
                    orfs.append(orf)
                else:


                    break

    return orfs

# #得到互补链的函数
def reverse_complement(sequence):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse = sequence[::-1]
    reverse_complement = ''.join([complement[base] for base in reverse])
    return reverse_complement

# 示例用法
dna_sequence = "ATGAAATAGTGA"
predicted_orfs1 = find_orf(dna_sequence)
predicted_orfs2 = find_orf(reverse_complement(dna_sequence))
print(reverse_complement(dna_sequence))
print("正向:{}".format(predicted_orfs1),"反向：{}".format(predicted_orfs2))





