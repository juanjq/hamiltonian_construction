import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np

import httpimport
with httpimport.remote_repo(['plt_config'], 'https://raw.githubusercontent.com/juanjq/matplotlib_configuration/main'):
     import plt_config
        
def plot(M, cmap='bwr', fsize=(5,5), norm=0):        
        
    plt_config.simple()

    fig, ax = plt.subplots(figsize=fsize)

    minmax = max([abs(np.amax(M)),abs(np.amin(M))])
    plot   = ax.imshow(M,cmap=cmap,vmin=-minmax,vmax=minmax, norm=colors.CenteredNorm(norm))
    plt.colorbar(plot)

    ax.axis('off')
