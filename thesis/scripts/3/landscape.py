import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.special import erf

alphas = np.linspace(1e-4, 1.5,100)

betas = np.linspace(-max(alphas), max(alphas),100)

def overlap2(alpha,beta):
    return np.exp(-(alpha-beta)**2)
def P(n,alpha,beta):
    if n==0:
        return overlap2(alpha,beta)
    else:
        return 1-overlap2(alpha,beta)

def kennedy(alpha):
    p=0
    for n in [0,1]:
        p+=np.max([P(n,ph*alpha,-alpha) for ph in [-1,1]])
    return p/2

def kennedy_opt(beta, alpha):
    p=0
    for n in [0,1]:
        p+=np.max([P(n,ph*alpha,beta) for ph in [-1,1]])
    return 1-p/2

def kennedy_opt_pr(beta, alpha,pr0=.5):
    p=0
    p+=np.exp(-np.abs(alpha + beta)**2)*pr0
    p+=(1-pr0)*(1-np.exp(-(alpha-beta)**2))
    return 1-p

aa= 1e-2
plt.plot(1-np.exp(-(aa-bets)**2))

from scipy.optimize import *
kennedys_opts = 1- np.array([minimize(kennedy_opt, -alpha, args=(alpha)).fun for alpha in alphas])

kenns = np.array([kennedy(a) for a in alphas])

def homodyne(alpha):
    return (1+erf(np.sqrt(2)*alpha))/2

def helstrom(alpha):
    return (1+np.sqrt(1-overlap2(alpha,-alpha)))/2

np.array([kennedy_opt_pr(-.5, aa, .5) for aa in alphas])

from scipy.optimize import *
### check###
# kennedys_opts_pr = 1- np.array([minimize(kennedy_opt_pr, -alpha, args=(alpha, .5)).fun for alpha in alphas])
# plt.plot(kennedys_opts_pr - kennedys_opts)
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

bets = np.linspace(0,10,10000)
kk= 1-kennedy_opt_pr(bets, 1e-3, .5)
mk = np.argmin(kk)
plt.figure(figsize=(12,12))
lw=5
tra = 0.8
ini=0
fini=int(.3*len(bets))
ax=plt.subplot()
ax.plot(bets, 1-kk ,linewidth=lw , alpha=tra)
axo=ax.inset_axes([.3,.3,.5,.4])
axo.plot(bets[ini:fini], (1-kk)[ini:fini] , linewidth=lw , alpha=tra)
ax.scatter(bets[mk], 1-kk[mk])
ax.set_ylim([.4,.51])
ep=.5*1e-2
mark_inset(ax, axo, loc1=2, loc2=1, fc="none", lw=.5, ec='r')
axo.set_ylim([.5-ep,.5+ep])
LS=20
axo.set_xticks([])
ax.set_xlabel(r'$\beta$',size=int(1.5*LS))
ax.set_ylabel(r'$P_S^{\beta-ken}(\alpha,\beta)$',size=int(1.5*LS))
ax.tick_params(axis='both', which='major', labelsize=LS)
ax.tick_params(axis='both', which='minor', labelsize=LS)
axo.tick_params(axis='both', which='major', labelsize=LS)
axo.tick_params(axis='both', which='minor', labelsize=LS)
path_dir = "Figures/313/"
os.makedirs(path_dir,exist_ok=True)
plt.savefig(path_dir+"kennedy_landscape.pdf")






### check Kennedy expression is correct ###

# np.array([kennedy(a) for a in alphas]) - (1-0.5*np.exp(-4*alphas**2))
# plt.plot(alphas,1-0.5*np.exp(-4*alphas**2))
# plt.plot(alphas, [kennedy(a) for a in alphas])
# aa = np.linspace(5,6,1000)
# alphas = aa
# plt.plot(alphas , homodyne(alphas) - (1-0.5*np.exp(-4*alphas**2)))







ax.plot(xalphas,kenns, color="green",,label=r'$P_S^{ken}$',linewidth=lw  alpha=tra)
ax.plot(xalphas,homodyne(alphas), color="blue",linewidth=lw,label=r'$P_S^{hom}$', alpha=tra)


plt.figure(figsize=(10,10))
LS=20
lw=5
tra = 0.8
xalphas = alphas**2
ax=plt.subplot()
ax.plot(xalphas,kenns, color="green",linewidth=lw ,label=r'$P_S^{ken}$', alpha=tra)
ax.plot(xalphas,homodyne(alphas), color="blue",linewidth=lw,label=r'$P_S^{hom}$', alpha=tra)
ax.plot(xalphas, kennedys_opts, color="red",linewidth=lw, label=r'$P_S^{ken-opt}$', alpha=tra)
ax.plot(xalphas, helstrom(alphas), color="black", linewidth=lw, label=r'$P_S^{hel}$', alpha=tra)
ax.set_xlabel(r'$|\alpha|^2$',size=int(1.5*LS))
ax.tick_params(axis='both', which='major', labelsize=LS)
ax.tick_params(axis='both', which='minor', labelsize=LS)
ax.legend(prop={"size":25})

path_dir = "Figures/312/"
os.makedirs(path_dir,exist_ok=True)
# plt.savefig(path_dir+"kennedy_compa.pdf")



plt.figure(figsize=(10,10))
LS=20
lw=5
tra = 0.8
ax=plt.subplot()
ax.plot(xalphas,helstrom(alphas)-np.array(kenns), color="green",linewidth=lw ,label=r'$P_S^{hel}-P_S^{ken}$', alpha=tra)
ax.plot(xalphas,helstrom(alphas)-homodyne(alphas), color="blue",linewidth=lw,label=r'$P_S^{hel}-P_S^{hom}$', alpha=tra)
ax.plot(xalphas, helstrom(alphas)-kennedys_opts, color="red",linewidth=lw, label=r'$P_S^{hel}-P_S^{ken-opt}$', alpha=tra)
ax.set_xlabel(r'$|\alpha|^2$',size=int(1.5*LS))
ax.tick_params(axis='both', which='major', labelsize=LS)
ax.tick_params(axis='both', which='minor', labelsize=LS)
ax.legend(prop={"size":25})
plt.savefig(path_dir+"kennedy_compa_diff_hel.pdf")


#

### landascape Kennedy
B=3.5
betas = np.linspace(-B,B,1000)
sbeta = 1-np.array([kennedy_opt(b, 0.2) for b in betas])
plt.figure(figsize=(10,10))
LS=20
lw=5
tra = 0.8
ax=plt.subplot()
ax.plot(betas, sbeta, color="green",linewidth=lw, alpha=tra, label=r'$P_s^{\beta-ken}(\alpha,\beta)$')
ax.set_xlabel(r'$\beta$',size=int(1.5*LS))
ax.axhline(homodyne(0.2), alpha=tra,linewidth=lw, label=r'$P_s^{hom}(\alpha)$')
ax.axvline(0.2,linestyle ='--',alpha=tra,linewidth=lw, color="black",label=r'$\beta = \pm \alpha$')
ax.axvline(-0.2, linestyle ='--', alpha=tra,linewidth=lw, color="black")#%, label=r'$\beta = -\alpha$')

# ax.set_ylabel(,size=int(1.5*LS))
ax.legend(prop={"size":25})
ax.tick_params(axis='both', which='major', labelsize=LS)
ax.tick_params(axis='both', which='minor', labelsize=LS)
ax.legend(prop={"size":20}, loc="upper left")
path_dir = "Figures/312/"
os.makedirs(path_dir,exist_ok=True)
plt.savefig(path_dir+"kenn_landscape.pdf")







#
