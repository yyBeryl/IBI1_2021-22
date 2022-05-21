import os
os.chdir("/Users/beryl/IBI1_2021-22/Practical8")
seq = open('sequence.fa','r')
#accept a new output of file name
filename=input("Please print the filename.")
yfile = open(filename+'.fa','w')#yfile is used for storage of the name of the gene and the number of cuts and the DNA sequence
fragment=" "#used for store sequence temporarily
for line in seq:
    line = seq.readline()
#read line without the line of the sequence information
    line = line.strip()
    if line.startswith('>')
        if 'GAATTC' in fragment:
#get the name of the gene
            for i in range(len(line)):
                if line[i:i+5]=="gene:":
                    name=''
                    n=i+5
                    while line[n]!=" ":
                        name+=line[n]
                        n=n+1
            m=fragment.find('GAATTC')#m is the number of cuts
            yfile.write(name+' '+str(m)+'\n'+fragment+'\n')
        fragment=" "#empty each time
        continue
    fragment+=line
#add the possible overlooked situation
if 'GAATTC' in fragment:
    for i in len(line):
        if "gene:"==line[i,i+5]:
            name=''
            n=i+5
            while line[n]!=" ":
                name+=line[n]
                n=n+1
    m=fragment.find('GAATTC')
    yfile.write(name +' '+ str(m)+'\n'+fragment+'\n')
yfile.close()
