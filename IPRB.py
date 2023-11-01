homodom=24
hetero=29
homorec=16

all=homodom+homorec+hetero
hethet=(hetero/all)*((hetero-1)/(all-1))*(1/4)
rechet=(homorec/all)*(hetero/(all-1))*(1/2)

hetrec=(hetero/all)*(homorec/(all-1))*(1/2)

recrec=(homorec/all)*((homorec-1)/(all-1))


print(1-(hethet+recrec+rechet+hetrec))