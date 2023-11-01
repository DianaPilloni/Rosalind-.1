def FASTA(file):
    read=open(file,'r')
    seq=read.readlines()
    seq=''.join(seq)
    new=[]

    new = []
    sequences = seq.split('>')
    for e in sequences:
        if e: 
            a = e.split('\n')
            DNAseq = ''.join(a[1:])
            new.append(DNAseq)
    return new
