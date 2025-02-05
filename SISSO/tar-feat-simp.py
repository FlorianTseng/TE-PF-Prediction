import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize

# Load data files
file_names = ['PFn-train.dat', 'PFp-train.dat']
targets = ['log($PF_n$)', 'log($PF_p$)']

# Select specific features for PFn and PFp datasets
selected_features_pfn = [r'${f_{\rm{p}}}$', r'$E_{\rm{g}}$', r'$\Delta {\bar r_{{\rm{cov}}}}$', r'$\bar \chi $']
data_pfn = pd.read_csv('PFn-train.dat', delimiter='\t')

selected_features_pfp = [r'${\bar N_{\rm{U}}}$', r'${\bar T_{\rm{M}}}$']
data_pfp = pd.read_csv('PFp-train.dat', delimiter='\t')

# Set up subplots
fig, axes = plt.subplots(3, 2, figsize=(7, 8))
axes = axes.flatten()

# Function to normalize colors
def normalize_colors(values, cmap_name):
    norm = Normalize(vmin=values.min(), vmax=values.max())
    cmap = plt.get_cmap(cmap_name)
    return cmap(norm(values))

# Plot selected features from PFn-train.dat
for i, feature in enumerate(selected_features_pfn):
    ax = axes[i]
    
    # Get feature and target data
    x = data_pfn[feature]
    y = data_pfn[targets[0]]
    
    # Normalize colors based on target values
    colors = normalize_colors(y, 'RdBu_r')
    
    # Scatter plot with black edge
    scatter = ax.scatter(x, y, c=colors, edgecolors='black', alpha=.8, s=25)
    ax.set_xlabel(feature, fontsize=12)
    ax.set_ylabel(targets[0], fontsize=12)
    ax.set_title(f'({chr(97 + i)}) {targets[0]} ~ {feature}', fontsize=12)
    
    # Set border width to 2
    for spine in ax.spines.values():
        spine.set_linewidth(2)

    ax.tick_params(direction='in', labelsize=12)
    ax.axvline(x=np.mean(x), color='black', linestyle='--', linewidth=2)

# Plot selected features from PFp-train.dat
for i, feature in enumerate(selected_features_pfp):
    ax = axes[i + len(selected_features_pfn)]
    
    # Get feature and target data
    x = data_pfp[feature]
    y = data_pfp[targets[1]]
    
    # Normalize colors based on target values
    colors = normalize_colors(y, 'RdBu_r')
    
    # Scatter plot with black edge
    scatter = ax.scatter(x, y, c=colors, edgecolors='black', alpha=.8, s=25)
    ax.set_xlabel(feature, fontsize=12)
    ax.set_ylabel(targets[1], fontsize=12)
    ax.set_title(f'({chr(101 + i)}) {targets[1]} ~ {feature}', fontsize=12)
    
    # Set border width to 2
    for spine in ax.spines.values():
        spine.set_linewidth(2)

    ax.tick_params(direction='in', labelsize=12)
    ax.axvline(x=np.mean(x), color='black', linestyle='--', linewidth=2)

# Adjust layout
plt.tight_layout()
plt.savefig('feat-tar.pdf', bbox_inches='tight')
plt.show()
