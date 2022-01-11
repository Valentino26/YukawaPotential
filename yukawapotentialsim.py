import numpy as np
import matplotlib.pyplot as plt


g = 1
#reduzierte Planksche Wirkungskonstante
h = 6.62606957 * 10**-34
h_s = h/np.pi * 2

c = 3*10**8

r = np.arange(0.01, 5, 0.0010,dtype= float)
def V_yukawa(m,r,g,h_s,c):
    result = (-g**2) * 1 *((np.e**((-m*r)/1))/r)
    return result

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel("Distance")
ax.set_ylabel("Potential Strength")
ax.grid()


for i in [0,1,2,3,4,10,50]:
    ax.plot(r, V_yukawa(i,r,1,h_s,c),label= f"m:{i}")

ax.set_ylim(-1,0.1)

m = [1,2,3,4,10,50]
ax.legend()
plt.show()
print(V_yukawa(1,r,1,h_s,c))
