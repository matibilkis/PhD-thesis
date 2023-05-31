import os
import sys
sys.path.insert(0, os.getcwd())

from qutip import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm

os.chdir("/home/mati/OneDrive/RESEARCH/PhDiaries/thesis/")


xcen=1
a = xcen/np.sqrt(2)
M=4
xvec = np.linspace(-5,5,200)
N = 50
rho1 = coherent_dm(N, a)
rho2 = coherent_dm(N, -a)

rho1at = coherent_dm(N, a+a)
rho2at = coherent_dm(N, -a+a)
rhoin = (rho1+rho2)/2
rhoout = (rho2at + rho1at)/2
wigner_in = wigner(rhoin,xvec,xvec)
wigner_out = wigner(rhoout, xvec, xvec)

fig=plt.figure(figsize=(10,10))
ax=plt.subplot()
Lx=max(xvec)
Ly=min(xvec)
l=.5
ls=20
ax.tick_params(axis='both', which='major', labelsize=20)
im1 = ax.contourf(xvec, xvec, wigner_in, 100, cmap=cm.RdBu, norm= mpl.colors.Normalize(-wigner_in.max(), wigner_in.max()))
ax.axvline(lw=l,color="black")
ax.axhline(lw=l,color="black")
fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.9, 0.15, 0.05, 0.7])
cc = fig.colorbar(im1, cax=cbar_ax)
cc.ax.tick_params(labelsize=10)
ax.set_title(r'$W(q,p)$',size=ls)

path_dir = "Figures/312/"
os.makedirs(path_dir,exist_ok=True)
plt.savefig(path_dir+"wigner_coh.pdf")






#
