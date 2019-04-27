from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
save_fig= "y"
x=[.015, .030, .045, .060, .075]
y=[0.01220231, 0.03060015, 0.04614136, 0.05900381, 0.06816518]

def test_func(x, a, b):
    return a *  x + b

params, params_covariance = optimize.curve_fit(test_func, x, y)
sigma = np.sqrt(np.diag(params_covariance))

f, ax = plt.subplots(1,1)
ax.scatter(x,y)
x_fit= np.linspace(0,0.1,1000)

print(params,sigma)

right_value_order = [params[0], sigma[0], params[1], sigma[1]]
legend = r"$f(x)=a\cdot x +b $ with""\n" \
         r"$a=%5.2f \pm %5.3f$ and " \
         r"$b=%5.2f \pm %5.3f$" % tuple(right_value_order)
plt.rc('text', usetex=True)
ax.plot(x_fit, test_func(x_fit, *params), label=legend)
ax.legend(shadow=True, loc=2, handlelength=1.5, fontsize=12)
plt.savefig('media/foo1.pdf')
plt.show()
