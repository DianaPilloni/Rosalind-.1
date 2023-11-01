a=input(f'dna\n')
s=[]
dictdna={'A':'T', 'C':'G' ,'G': 'C', 'T':'A'}
for el in a:
    s.append(dictdna[el])

s.reverse()
print(''.join(s))