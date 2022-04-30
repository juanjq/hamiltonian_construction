import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np

#matplotlib configuration
import httpimport
with httpimport.remote_repo(['plt_config'], 'https://raw.githubusercontent.com/juanjq/matplotlib_configuration/main'):
     import plt_config

#plot function
def plot(M, cmap='bwr', fsize=(5,5), norm=None):        
        
    #simple configuration
    plt_config.simple()

    fig, ax = plt.subplots(figsize=fsize)

#     minmax = max([abs(np.amax(M)),abs(np.amin(M))])   #,vmin=-minmax,vmax=minmax

    #plotting the matrix
    if norm != None:
          plot = ax.imshow(M,cmap=cmap, norm=colors.CenteredNorm(norm))
    else:
          plot = ax.imshow(M,cmap=cmap)
    plt.colorbar(plot)

    ax.axis('off')
