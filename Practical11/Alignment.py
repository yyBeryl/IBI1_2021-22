import os
import pandas as pd
import numpy as np
os.chdir("/Users/beryl/IBI1_2021-22/Practical11")
seqh=open('DLX5_human.fa','r')
seqm=open('DLX5_mouse.fa','r')
seqr=open('RandomSeq.fa','r')
h=[]
m=[]
r=[]
for line in seqh:
    line=line.strip()
    if line.startswith('>'):
        continue
    h.append(line)
for line in seqm:
    line=line.strip()
    if line.startswith('>'):
        continue
    m.append(line)
for line in seqr:
    line=line.strip()
    if line.startswith('>'):
        continue
    r.append(line)
h=''.join(h)
m=''.join(m)
r=''.join(r)
class Comparison():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def com(self):
        identical=0
        for i in range(len(h)):
            if self.a[i]==self.b[i]:
                identical+=1
        return identical
    def COM(self):
        s_list=[]
        blosum=pd.read_csv("BLOSUM.csv")
        c=list(blosum.head())
        for i in range(len(h)):
            column=[]
            for k in range(len(c)):
                if c[k]==self.a[i]:
                    column.append(True)
                else:
                    column.append(False)
            result1=blosum.loc[(blosum['First']==self.b[i]),column]
            result_1=result1.iloc[0,0]
            s=''.join(str(result_1))
            s_list.append(s)
        int_list=[int(x) for x in s_list]
        S=sum(int_list)
        return S
A=Comparison(h,m)
B=Comparison(h,r)
C=Comparison(r,m)
print("The percentage of identical amino acids for human sequence and mouse sequence is "+str(Comparison.com(A)/len(h))+", and the score is "+str(Comparison.COM(A))+".")
print("The percentage of identical amino acids for human sequence and random sequence is " +str(Comparison.com(B)/len(h))+", and the score is "+str(Comparison.COM(B))+".")
print("The percentage of identical amino acids for random sequence and mouse sequence is "+str(Comparison.com(C)/len(h))+", and the score is "+str(Comparison.COM(C))+".")