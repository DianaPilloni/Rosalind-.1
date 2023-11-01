def FIBD(m,n):
    gen = [0] * n
    gen[0] = 1
        
    for rabbit in range(m-1):
        new_gen = 0
        for i in range(n-1,0,-1):
            new_gen += gen[i]
            gen[i] = gen[i-1]
        gen[0] = new_gen
    return sum(gen)

print(FIBD(96,17))