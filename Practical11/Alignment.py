import os
import pandas as pd
import numpy as np
os.chdir("/Users/beryl/IBI1_2021-22/Practical11")
seqh=open('DLX5_human.fa','r')
seqm=open('DLX5_mouse.fa','r')
seqr=open('RandomSeq.fa','r')
#create three empty lists for temporary storage of sequences
h=[]
m=[]
r=[]
for line in seqh:
#read only gene itself
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
#use join to make the elements in the list into new strings
h=''.join(h)
m=''.join(m)
r=''.join(r)
#use class to make two variables change together
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
        c=list(blosum.head())#c is the animo acids in blosum
        for i in range(len(h)):
#add the same animo acids
            column=[]
            for k in range(len(c)):
                if c[k]==self.a[i]:
                    column.append(True)
                else:
                    column.append(False)
            result1=blosum.loc[(blosum['First']==self.b[i]),column]#result1 is showing needed all situations 
            result_1=result1.iloc[0,0]#get the numbers
            s=''.join(str(result_1))#change to strings
            s_list.append(s)#change to list
        int_list=[int(x) for x in s_list]#change strings to numbers
        S=sum(int_list)#calculate the scores
        return S
#enter variables in pairs 
A=Comparison(h,m)
B=Comparison(h,r)
C=Comparison(r,m)
#calculate the percentage and print the results
print("The percentage of identical amino acids for human sequence and mouse sequence is "+str(Comparison.com(A)/len(h))+", and the score is "+str(Comparison.COM(A))+".")
print("The percentage of identical amino acids for human sequence and random sequence is " +str(Comparison.com(B)/len(h))+", and the score is "+str(Comparison.COM(B))+".")
print("The percentage of identical amino acids for random sequence and mouse sequence is "+str(Comparison.com(C)/len(h))+", and the score is "+str(Comparison.COM(C))+".")
#Summary
#Results
#The percentage of identical amino acids for human sequence and mouse sequence is 0.9653979238754326, and the score is 1490.
#The percentage of identical amino acids for human sequence and random sequence is 0.02768166089965398, and the score is -351.
#The percentage of identical amino acids for random sequence and mouse sequence is 0.031141868512110725, and the score is -348.
#Interpretation
#The DLX5 protein in human and mouse is quite similar, the percentage of identical amino acids and the score are both very high. This suggests that the DLX5 gene changed little over the course of biological evolution.
