import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import normaltest

pts = 1000
np.random.seed()
a = np.random.normal(0, 1, size=pts)
b = np.random.normal(2, 1, size=pts)
# plt.plot(a)
# plt.plot(b)
# plt.show()
x = np.concatenate((a, b))
# x = stats.norm.rvs(size = 1000)
plt.hist(x)
plt.show()
k2, p = normaltest(x)
alpha = 1e-3
print("p = {:g}".format(p))
if p < alpha:  # null hypothesis: x comes from a normal distribution
    print("The nullhypothesis is bad")
else:
    print("The nullhypothesis is good")

