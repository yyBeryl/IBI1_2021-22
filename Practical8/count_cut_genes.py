import os
os.chdir("/Users/beryl/IBI1_2021-22/Practical8")
seq = open('sequence.fa','r')
filename=input("Please print the filename.")
yfile = open(filename+'.fa','w')
fragment=" "
for line in seq:
    line = seq.readline()
    line = line.strip()
    if line.startswith('>'):
        if 'GAATTC' in fragment:
            for i in range(len(line)):
                if line[i:i+5]=="gene:":
                    name=''
                    n=i+5
                    while line[n]!=" ":
                        name+=line[n]
                        n=n+1
            m=fragment.find('GAATTC')
            yfile.write(name+' '+str(m)+'\n'+fragment+'\n')
        fragment=" "
        continue
    fragment+=line
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