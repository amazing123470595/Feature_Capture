file = 'Training' # 输入文件名（不带后缀）
input_file = 'data/' + file + '.txt'
pos_output = 'MyData/pos_' + file + '.fasta'
neg_output = 'MyData/neg_' + file + '.fasta'

with open(input_file, 'r') as f:
    lines = f.readlines()

pos_lines = []
neg_lines = []

for i in range(0, len(lines), 2):
    header = lines[i].strip()
    sequence = lines[i+1].strip()
    if header.startswith('>Pos'):
        pos_lines.append(f"{header}\n{sequence}\n")
    elif header.startswith('>Neg'):
        neg_lines.append(f"{header}\n{sequence}\n")

with open(pos_output, 'w') as f:
    f.writelines(pos_lines)

with open(neg_output, 'w') as f:
    f.writelines(neg_lines)

print(f"处理完成：正样本数：{len(pos_lines)}，负样本数：{len(neg_lines)}")