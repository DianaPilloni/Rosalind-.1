import re
with open ('Homework to submit\protein masses.txt','r') as file:
    read=file.readlines()
    
read=''.join(read)
read=read.split('\n')
dict_proteinmass={}
for el in read:
    s=re.split('(.)   (.*)',el)
    s.remove('')
    s.remove('')
    dict_proteinmass[f'{s[0]}']=float(s[1])

sum=0
protein='ERNVMPIMSDRFWYWHDFLKLKQYPPKWDKAWKFKACMCFICVIDSLMAEQQYALVHYNGNICNPFERDSYLKEDVMRGENIINAPWKGMCGGPIPAICQAPWQASAPQMRNCAPEIPAVHDAWRQQDQKGQGPSSILCCCGIDTPPGAHDYSLKQFWQIFGISDATHEMICRASKANKTQLTGARSFRQHEESMLLMWETNQPRGCWWLHFRTALMECCQTIRGDCQQRRWESAPMMLNFWGAIAYVGMSRTLINNDKCMLPPAVHGMNDPVRFASSMLAYCAVMFNDPQGMYVDLRKSIQMDCAQQLWDWAGYQTDNLRAHIALVVIMCLPVWLIQHKTKPQGFLRVQMNVDMKRNYMRYWKGGYGYWVAWMFKCCEHGFEQNPAGLIWAHTREGDTYQAPREWTAYRWPVMGQLHALSYNVAPMNVCWRQCRMNFSIHHMISGCFGFDSDSPWWFYPNGYDFKPPTMLRCPFPGFSDYNRTSTYKNNSIYHLKMGLLWRLENRKQQFSFSLLVVVQKNSHWDPVMIYNDIRAIRMNEVKITVPQKIYRMHGYYITSCHRIKTGPCHCPRIQNHSVAEGCKLDPQPNECYHLKVWYEADQKAPLEFPTHIQGDEMDCWLQEHDTIITRCRLWPAITENGDKWEEGNTCLIWENAFIPHNWAFCFNHKDFVTQEISIAYNMENDMSQCWMDPTHGYTWLAQVDGASLKTQETAGAQEHAKNMKIWLHADHCWHSNWDGYWMDVSPKSHLFNAGGGIYVHWRFNLWAHDINCFHSDPNIWSDTRIHFCRRSNHAAMALIKESQDVPYKISNAGKYQLGLNV'
for letters in protein:
    sum+=dict_proteinmass[letters]

print(sum)

