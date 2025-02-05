import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# 读取所有七大晶系文件夹
crystal_systems = ['Cubic', 'Tetragonal', 'Orthorhombic', 'Hexagonal', 'Trigonal', 'Monoclinic', 'Triclinic']

# 用于保存晶系n型和p型的$R^2$值
n_type_r2 = []
p_type_r2 = []
crystal_labels = []

# 遍历每个晶系的文件夹
for crystal in crystal_systems:
    # 构建n型和p型测试集文件路径
    n_test_file = os.path.join(f'{crystal}_results', f'{crystal}_PF_n.csv')
    p_test_file = os.path.join(f'{crystal}_results', f'{crystal}_PF_p.csv')

    # 读取n型和p型测试集的csv文件
    n_test_df = pd.read_csv(n_test_file)
    p_test_df = pd.read_csv(p_test_file)

    # 计算n型和p型的$R^2$值
    n_r2 = r2_score(n_test_df['True Value'], n_test_df['Predicted Value'])
    p_r2 = r2_score(p_test_df['True Value'], p_test_df['Predicted Value'])

    # 保存晶系名和对应的$R^2$值
    crystal_labels.append(crystal)
    n_type_r2.append(n_r2)
    p_type_r2.append(p_r2)

# 绘制柱状图
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# n型$R^2$值柱状图
axes[0].bar(crystal_labels, n_type_r2, color=(0.4, 0.6, 1), edgecolor='black')
axes[0].set_title('n-type $R^2$ by Crystal System', fontsize=14, fontname='Arial')
axes[0].set_xlabel('Crystal System', fontsize=14, fontname='Arial')
axes[0].set_ylabel('Test $R^2$', fontsize=14, fontname='Arial')
axes[0].set_xticklabels(crystal_labels, rotation=90, fontsize=12, fontname='Arial')

# p型$R^2$值柱状图
axes[1].bar(crystal_labels, p_type_r2, color=(1, 0.6, 0.6), edgecolor='black')
axes[1].set_title('p-type $R^2$ by Crystal System', fontsize=14, fontname='Arial')
axes[1].set_xlabel('Crystal System', fontsize=14, fontname='Arial')
axes[1].set_ylabel('Test $R^2$', fontsize=14, fontname='Arial')
axes[1].set_xticklabels(crystal_labels, rotation=90, fontsize=12, fontname='Arial')

# 为每个柱子加上$R^2$值标签
for ax, r2_values in zip(axes, [n_type_r2, p_type_r2]):
    for i, r2 in enumerate(r2_values):
        ax.text(i, r2 + 0.001, f'{r2:.2f}', ha='center', va='bottom', fontsize=14, fontname='Arial')

# 刻度线朝内
for ax in axes:
    ax.tick_params(axis='both', direction='in')

# 自动调整子图间距
plt.tight_layout()

# 显示图像
plt.show()
