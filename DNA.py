a=input("what's the DNA?\n")
from collections import Counter
'''we can use the counter function, but the result will be in the form
Counter({'A': 201, 'G': 201, 'C': 200, 'T': 199})
so we need another method'''

dict_count={'A':0, 'C':0 ,'G': 0, 'T':0}
for s in a:
    dict_count[s]=dict_count[s]+1
print (f"{dict_count['A']} {dict_count['C']} {dict_count['G']} {dict_count['T']}")