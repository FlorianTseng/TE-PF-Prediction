import pandas as pd
import matplotlib.pyplot as plt
import os

# 读取数据文件
file_names = ['PFn-train.dat', 'PFp-train.dat']
targets = ['log($PF_n$)', 'log($PF_p$)']

# 设置子图布局
fig, axes = plt.subplots(4, 6, figsize=(16, 14))
axes = axes.flatten()

# 读取并绘制每个文件的数据
offset = 0
for file_name, target in zip(file_names, targets):
    data = pd.read_csv(file_name, delimiter='\t')
    features = data.columns[2:]

    # 逐个特征绘制散点图
    for i, feature in enumerate(features):
        ax = axes[i + offset]
        scatter = ax.scatter(data[feature], data[target], alpha=0.6, s=10, 
                             edgecolors='black', c=data[target], cmap='RdBu_r')
        ax.set_xlabel(feature, fontsize=10)
        ax.set_ylabel(target, fontsize=10)
        ax.set_title(f'{target} ~ {feature}', fontsize=12)

        # 将坐标轴刻度线改为朝内
        ax.tick_params(axis='both', direction='in', labelsize=10)

    # 更新偏移量
    offset += len(features)

# 调整布局
plt.tight_layout()
plt.show()
