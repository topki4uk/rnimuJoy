import os

file_list = os.listdir(r'alightments')

seqs_dict = {}

for file in file_list:
    with open(f'alightments/{file}', 'r') as protein:
        fasta_file = protein.read().split()

        name_list = fasta_file[::2]
        seq_list = fasta_file[1::2]

        seq_dict = dict(zip(name_list, seq_list))

        for name, seq in seq_dict.items():
            if name not in seqs_dict.keys():
                seqs_dict[name] = seq
            else:
                seqs_dict[name] += seq

with open(r'new_full.fasta', 'w') as file:
    string = ''
    for name, seq in seqs_dict.items():
        string += f'{name}\n'
        string += f'{seq}\n'

    file.write(string)
