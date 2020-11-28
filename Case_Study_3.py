import math
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

'''
Part III B
'''
Co = 30 #mg/L
k = 0.03 # 1/day
Xmax = 12 #m
porosity = 0.3
De = 525 * 0.0001 #cm^2/day * 0.0001 m^2/cm^2
alpha = (Co)/(1+math.exp(2*math.sqrt(k*porosity/De)*Xmax))
beta = (Co)/(1+math.exp(-2*math.sqrt(k*porosity/De)*Xmax))
print(alpha)
print(beta)
x = []
#generate the list for x from 0 to 12 here
for ii in range(13):
    x.append(ii)
C = []
#generate the list for concentration at 13 points here
for item in x:
    C.append(alpha*math.exp(math.sqrt(k*porosity/De)*item)+beta*math.exp(-math.sqrt(k*porosity/De)*item))

#this generates the plot we need
from matplotlib import pyplot as plt
fig, ax = plt.subplots()
ax.plot(x, C)
ax.set_xlabel('Position x in Biofilm Reactor (m)')
ax.set_ylabel('Concentration of Organic Matter (mg/L)')
ax.set_title('Concentration of Organic Matter (mg/L) vs Position in Biofilm Reactor (m)')

'''
Part III C
'''
x_no_sub = [0,1,2,3,4,5,5.1,5.2,5.3,5.4,5.5,5.51,5.552,5.553,5.554,5.555,5.565,5.57291]
x_sub = [5.57292,6,7,8,9,10,11,12]
P_no1 = []
P_no2 =[]
P_no3 = []
P_no4 = []
P_no5 = []
#generate list for lines without subsidy
for item in x_no_sub:
    P_no1.append(250*12*3*1 - (300*item**2+500*1))
    P_no2.append(250*12*3*2 - (300*item**2+500*2))
    P_no3.append(250*12*3*3 - (300*item**2+500*3))
    P_no4.append(250*12*3*4 - (300*item**2+500*4))
    P_no5.append(250*12*3*5 - (300*item**2+500*5))
print('P(3.34997) = ' + str(250*12*3*1 - (300*3.34997**2+500*1)))
P_sub1 = []
P_sub2 =[]
P_sub3 = []
P_sub4 = []
P_sub5 = []
for item in x_sub:
    P_sub1.append((250*12*3+12*365)*1 - (300*item**2+500*1))
    P_sub2.append((250*12*3+12*365)*2 - (300*item**2+500*2))
    P_sub3.append((250*12*3+12*365)*3 - (300*item**2+500*3))
    P_sub4.append((250*12*3+12*365)*4 - (300*item**2+500*4))
    P_sub5.append((250*12*3+12*365)*5 - (300*item**2+500*5))
print('P(5.57292) = ' + str((250*12*3+12*365)*1 - (300*5.57292**2+500*1)))
P1 = P_no1 + P_sub1
P2 = P_no2 + P_sub2
P3 = P_no3 + P_sub3
P4 = P_no4 + P_sub4
P5 = P_no5 + P_sub5
Xtotal = x_no_sub + x_sub
zero = []
for item in Xtotal:
    zero.append(0)

#this generates the plot we need
fig2, ax2 = plt.subplots()
ax2.plot(Xtotal, P1, label = 'Year 1')
ax2.plot(Xtotal, P2, label = 'Year 2')
ax2.plot(Xtotal, P3, label = 'Year 3')
ax2.plot(Xtotal, P4, label = 'Year 4')
ax2.plot(Xtotal, P5, label = 'Year 5')
ax2.plot(Xtotal, zero, linestyle = 'dashed', color='red', label = 'Break Even Point')
ax2.axvline(x = 5.57292, ymin = -200000, ymax = 200000, linestyle = ':', color = 'gray', alpha = 0.8, label='Max Profit')
ax2.axvline(x = 3.34997, ymin = -200000, ymax = 200000, linestyle = '-.', color = 'gray', alpha = 0.8, label='Min Length')
ax2.set_xlabel('Total Length of Reactor (m)')
ax2.set_ylabel('Profit ($)')
ax2.set_title('Profit ($) vs. Total Length of Reactor (m) From Year 1-5')
plt.legend()
plt.show()