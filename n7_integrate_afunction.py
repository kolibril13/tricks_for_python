import numpy as np
from scipy.integrate import quad

def integrand(x):
    return np.sin(x)

ans = quad(integrand, 0, np.pi)[0]
print(ans)
