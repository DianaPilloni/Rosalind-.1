from fastafunction import FASTA
import re
from translator import codon_dict
new=FASTA('Homework to submit\FASTAsplc.txt')

DNA =new[0]

new.remove(DNA)
for el in new:
    if el in DNA:
        DNA=DNA.replace(el,'')

def toprot(DNA):
    
    RNA=DNA.replace('T','U')
    
    RNA=re.split(r'([AUGC]{3})',RNA)

    
    aminosequence=[]
    for elements in RNA:
        if elements != '':
            if codon_dict[elements] != 'stop':
                aminosequence.append(codon_dict[elements])
            else:
                break

    #now we join the aminoacids
    protein=''.join(aminosequence)
    return protein

print(toprot(DNA))
