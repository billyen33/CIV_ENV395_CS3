
'''
Part II A
'''
#stuff the 2 bacteria share
Q = 40 #m^3/day
V = 700 #m^3
So = 100 #mg/L

#bacterium 1
umax1 = 2.2 #1/day
Ks1 = 22 #mg/L
Kd1 = 1.1 #1/day

#bacterium 2
umax2 = 1.8 #1/day
Ks2 = 25 #mg/L
Kd2 = 0.95 #1/day

S1 = (Ks1*(Q/V + Kd1))/(umax1-(Q/V+Kd1))
S2 = (Ks2*(Q/V + Kd2))/(umax2-(Q/V+Kd2))
print("S1= " + str(S1) + " mg/L")
print("S2= " + str(S2) + " mg/L")

#now determine efficiencies
E1 = (So-S1)/So * 100
E2 = (So-S2)/So * 100
print("E1= " + str(E1))
print("E2= " + str(E2))

'''
Part II B
'''
P = 36.1 #mg/L
Yxs = 1.5 #mg cells/mg OM
Yps = 1.3 #mg CO2/mg OM
m = 0 #assume negligible

Pin = 0#P - Yps*(So-S2) #the steady state S is what we calculated in 2A, unit is mg CO2/L
#print(So-S2)
omega = ((((umax2*S2)/((Ks2+S2)*Yxs))+m)*(P-Pin))/((So-S2)*(1-((P-Pin)/(Yps*(So-S2)))))
print("omega= " + str(omega) + " mg CO2/(day*mg cells)")