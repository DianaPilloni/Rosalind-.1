t=input(f'dna\n')
t=list(t)
for el in t:
    if el=='T':
        t[t.index(el)]='U'

print(''.join(t))