import os
os.chdir("/Users/beryl/IBI1_2021-22/Practical8")
seq = open('sequence.fa','r')#read the original fasta file
temporary=" "#create a blank string to store sequences temporarily
xfile = open('cut_genes.fa','w')#create a new file cut_gene.fa
for line in seq:
#read line without the line containing the name of genes
    line = seq.readline()
    line = line.strip()
    if line.startswith('>'):
	#write sequences that can be cut in xfile
        if 'GAATTC' in temporary:
            xfile.write(temporary+'\n')
        temporary=" "#empty the string each time
        continue
    temporary+=line
if 'GAATTC' in temporary:
    xfile.write(temporary+'\n')#write the target sequences to the x file
xfile.close()
