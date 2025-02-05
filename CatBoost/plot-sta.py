import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 数据文件
pf_dataset_file = "E:\paper1-2025\CraTENet-main\dataset\pf-dataset.csv"
pf_n_file = "PF_n.csv"
pf_p_file = "PF_p.csv"

# 加载数据
df = pd.read_csv(pf_dataset_file)
df_n = pd.read_csv(pf_n_file)
df_p = pd.read_csv(pf_p_file)

# 提取 'type' 列为 n 和 p 的样本，并提取 '300' 列
data_n = df[df['type'] == 'n']['300']
data_p = df[df['type'] == 'p']['300']

# 提取指定列
log_pf_n = df_n['log(PF_n)']
log_pf_p = df_p['log(PF_p)']

# 全局样式设置
plt.rcParams['font.family'] = 'Arial'        # 设置字体为 Arial
plt.rcParams['font.size'] = 14               # 设置字体大小为 14
plt.rcParams['axes.linewidth'] = 2           # 设置坐标轴边框线宽为 2
plt.rcParams['xtick.direction'] = 'in'       # 设置 x 轴刻度线朝内
plt.rcParams['ytick.direction'] = 'in'       # 设置 y 轴刻度线朝内
plt.rcParams['xtick.major.width'] = 2        # 设置 x 轴主刻度线宽度为 2
plt.rcParams['ytick.major.width'] = 2        # 设置 y 轴主刻度线宽度为 2

# 创建子图
fig, axes = plt.subplots(1, 2, figsize=(16, 6), constrained_layout=True)

# 子图 1: 300 列的 n 和 p 类型样本分布
sns.kdeplot(data_n, label="n-type at 300K", fill=True, alpha=0.5, color="blue", ax=axes[0])
sns.kdeplot(data_p, label="p-type at 300K", fill=True, alpha=0.5, color="orange", ax=axes[0])
axes[0].set_title("PF Distribution Curve at 300K & 10$^{18}$ cm$^{-3}$\nRef: Mach. Learn.: Sci. Technol. 4 (2023) 015037")
axes[0].set_xlabel("Property Value at 300K")
axes[0].set_ylabel("Density")
axes[0].legend(fontsize=14, loc='best', frameon=False)

# 子图 2: log(PF_n) 和 log(PF_p) 的分布
sns.kdeplot(log_pf_n, label="log($PF_n$)", fill=True, alpha=0.5, ax=axes[1])
sns.kdeplot(log_pf_p, label="log($PF_p$)", fill=True, alpha=0.5, ax=axes[1])
axes[1].set_title("Distribution Curve of $\log(PF)$ (Our work)")
axes[1].set_xlabel("log(PF)")
axes[1].set_ylabel("Density")
axes[1].legend(fontsize=14, loc='best', frameon=False)

# 显示图形
plt.show()
