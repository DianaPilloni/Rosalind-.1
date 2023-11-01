import re
from Bio import SeqIO
from Bio.Seq import Seq
read=open('Homework to submit\FASTAgc.txt','r')

a=re.compile('>Rosalind_....\n')
dict=SeqIO.to_dict(SeqIO.parse(read,'fasta'))
percentage=0
rosalind=''
for key in dict:
    g=dict[key].count('G')
    c=dict[key].count('C')
    temp=((g+c)/len(dict[key]))
    if temp>percentage:
        percentage=temp
        rosalind=key

print(f'{rosalind}\n{percentage*100}')
    