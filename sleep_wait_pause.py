import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import zero_Celsius
plt.rcParams['figure.dpi'] = 150

Tmax = zero_Celsius +300
Tmin = zero_Celsius +20
R = 8.314
kappa = 5/3
V1= 1
V2= 2

p1 = R*Tmax/V1
p2 = p1*V1/V2

V3 = (Tmax/Tmin * V2**(kappa-1))**(1/(kappa-1))
p3 = p2* V2**kappa / V3**kappa

V4 = (Tmax/Tmin * V1**(kappa-1))**(1/(kappa-1))
p4 = p3*V3/V4

V12 = np.linspace(V1,V2,100)
V23 = np.linspace(V2,V3,100)
V34 = np.linspace(V3,V4,100)
V41 = np.linspace(V4,V1,100)

def p_isotherm(V,T):
    return (R*T)/V

def p_adiabatisch(V,p_start,v_start):
    return (p_start*v_start**kappa)/V**kappa



plt.plot(V12, p_isotherm(V12,Tmax),label = f"Tmax = {Tmax-zero_Celsius:.0f} °C")
plt.plot(V23, p_adiabatisch(V23, p2,V2),label = f"Adia")
plt.plot(V34, p_isotherm(V34,Tmin),label = f"Tmin = {Tmin-zero_Celsius:.0f} °C")
plt.plot(V41, p_adiabatisch(V41, p4,V4),label = f"Adia2")


plt.legend()
plt.scatter(V1,p1)
plt.scatter(V2,p2)
plt.scatter(V3,p3)
plt.scatter(V4,p4)

plt.ylabel("Druck [Pa]")
plt.xlabel("Volumen [m$^3$]")
plt.ticklabel_format(axis="x", style="sci", scilimits=(0,5))
