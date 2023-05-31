import qutip
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib import cm


N = 50

rho_coh = qutip.coherent(N,np.sqrt(2)*0.0)

x = np.linspace(-3,3,301)
W = qutip.wigner(rho_coh,x,x)

#W = np.around(W,decimals=4)

LS = 30
fig=plt.figure(figsize=(12,12))
ax = plt.subplot()
wmap = qutip.wigner_cmap(W)
nrm = matplotlib.colors.Normalize(W.min(), W.max())
im=ax.contourf(x, x, W, 300, cmap=cm.RdPu, norm=nrm)
cb1 = fig.colorbar(im, ax=ax)
cb1.ax.tick_params(labelsize=20)
ax.set_xlabel(r'$q$',size=int(1.5*LS))
ax.set_ylabel(r'$p$',size=int(1.5*LS))
ax.tick_params(axis='both', which='major', labelsize=LS)
ax.tick_params(axis='both', which='minor', labelsize=LS)
plt.savefig("figures/vacuum.png",dpi=200)
]
