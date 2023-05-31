import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt


import os
def helstrom(c):
    return (1 - np.sqrt(1-c**2))*.5
cs=np.linspace(0,1,1000)
plt.figure(figsize=(20,10))
ax = plt.subplot(111)
LS = 20
ax.tick_params(axis='both', which='major', labelsize=LS)
ax.tick_params(axis='both', which='minor', labelsize=LS)
ax.plot(cs,helstrom(cs), linewidth=int(LS/2), color="red",alpha=.75)
ax.set_xlabel(r'$|c|$',size=int(2*LS))
ax.set_ylabel(r'$P_e(\mathcal{M}^*)$', size=int(2*(LS)))
# plt.show()

os.makedirs("../figures/", exist_ok=True)
plt.savefig("../figures/helstrom_pure.pdf")
