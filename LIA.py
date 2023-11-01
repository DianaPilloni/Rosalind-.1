'''
probability that in the k-th generation at least N are Aa Bb
prob that Aa Bb mating with same genotype > 4/9



'''

import math
def com_fun(n,r):
    f = math.factorial
    return f(n)/f(r)/f(n-r)

def LIA(k,n):
    probhet = 4/16
    prob = []
    tot = 2**k
    for i in range(n,(tot+1)):
        prob.append(com_fun(tot,i)*(probhet**i)*((1-probhet)**(tot-i)))
    return sum(prob)
    

print(LIA(6,15))