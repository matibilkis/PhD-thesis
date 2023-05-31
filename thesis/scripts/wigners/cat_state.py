import qutip
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib import cm


N = 300
x = np.linspace(-5,5,101)
al = .6
rho1 = qutip.coherent(N,2) + qutip.coherent(N,-2)

W = qutip.wigner(rho1,x,x)


import os
os.makedirs("figures",exist_ok=True)


LS = 30
fig=plt.figure(figsize=(10,10))
ax = plt.subplot()
wmap = qutip.wigner_cmap(W)
nrm = matplotlib.colors.Normalize(W.min(), W.max())
im=ax.contourf(x, x, W, 100, cmap=cm.RdPu, norm=nrm, alpha=1)
cb1 = fig.colorbar(im, ax=ax)
cb1.ax.tick_params(labelsize=20)
ax.set_xlabel(r'$q$',size=int(1.5*LS))
ax.set_ylabel(r'$p$',size=int(1.5*LS))
ax.tick_params(axis='both', which='major', labelsize=LS)
ax.tick_params(axis='both', which='minor', labelsize=LS)
plt.savefig("figures/cat.png")
