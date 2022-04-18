import os
os.chdir("/Users/beryl/IBI1_2021-22/Practical8")
seq = open('sequence.fa','r')
temporary=" "
xfile = open('cut_genes.fa','w')
for line in seq:
    line = seq.readline()
    line = line.strip()
    if line.startswith('>'):
        if 'GAATTC' in temporary:
            xfile.write(temporary+'\n')
        temporary=" "
        continue
    temporary+=line
if 'GAATTC' in temporary:
    xfile.write(temporary+'\n')
xfile.close()