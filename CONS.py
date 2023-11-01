
from fastafunction import FASTA

new=FASTA('Homework to submit\FASTAcons.txt')

len=len(new[0])
final={'A':[0]*len,'T':[0]*len,'C':[0]*len,'G':[0]*len}
a=0
for seq in new:
    for let in seq:
        final[let][a]+=1
        a+=1
    a=0

finalseq=[0]*len
a=0
cons=['']*len
for key in final:
    while a < len:
        if final[key][a]>finalseq[a]:
            finalseq[a]=final[key][a]
            cons[a]=key
        a+=1
    a=0
print(''.join(cons))

for key in final:
    print(f'{key}: {" ".join(map(str, final[key]))}')