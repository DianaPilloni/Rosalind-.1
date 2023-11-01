from fastafunction import FASTA

seq=FASTA('Homework to submit\FASTAtrans.txt')
print(seq)
transitions=0
transversions=0
change=0
for a in range(0,len(seq[0])):
    if seq[0][a]!=seq[1][a]:
        change +=1
        if seq[0][a]=='G' and seq[1][a]=='A' or seq[0][a]=='A' and seq[1][a]=='G':
            transitions+=1
        elif seq[0][a]=='T' and seq[1][a]=='C'or seq[0][a]=='C' and seq[1][a]=='T':
            transitions+=1
        else:
            transversions+=1

print(transitions/transversions)
