
#Part II A
'''
Define all constants here
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
umax2 = 1.8
Ks2 = 25
Kd2 = 0.95

S1 = (Ks1*(Q/V + Kd1))/(umax1-(Q/V+Kd1))
S2 = (Ks2*(Q/V + Kd2))/(umax2-(Q/V+Kd2))
print("S1= " + str(S1) + " mg/L")
print("S2= " + str(S2) + " mg/L")

#now determine efficiencies
E1 = (So-S1)/So * 100
E2 = (So-S2)/So * 100
print("E1= " + str(E1))
print("E2= " + str(E2))

#Part II B
