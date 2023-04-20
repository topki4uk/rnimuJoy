import os

file_list = os.listdir(r'alightments')

gen_list = []
name_list = []

for file in file_list:
    with open(f'alightments/{file}', 'r') as protein:
        read = protein.read().split()
        if not name_list:
            name_list = read[::2]
        gen_list.append(
            read[1::2]
        )

gens = []

for i in range(23):
    s = ''
    for j in range(6):
        s += gen_list[j][i]

    gens.append(s)


with open('full.fasta', 'w') as file:
    s = ''

    for i in range(len(gens)):
        s += f'{name_list[i]}\n{gens[i]}\n'

    file.write(s)
