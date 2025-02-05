import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from matplotlib import rcParams
import seaborn as sns

# 设置字体为微软雅黑
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 读取数据
data_n = np.genfromtxt('PFn.dat', skip_header=1, usecols=(1, 2, 3, 4, 5))
data_p = np.genfromtxt('PFp.dat', skip_header=1, usecols=(1, 2, 3, 4, 5))

# 提取真实值和预测值
ktrue_n = data_n[:, 0]
ksisso_n = data_n[:, 1]
descriptor_1_n = data_n[:, 2]
descriptor_2_n = data_n[:, 3]
descriptor_3_n = data_n[:, 4]

ktrue_p = data_p[:, 0]
ksisso_p = data_p[:, 1]
descriptor_1_p = data_p[:, 2]
descriptor_2_p = data_p[:, 3]
descriptor_3_p = data_p[:, 4]

# 计算R^2、RMSE和MAE
r2_n = r2_score(ktrue_n, ksisso_n)
rmse_n = np.sqrt(mean_squared_error(ktrue_n, ksisso_n))
mae_n = mean_absolute_error(ktrue_n, ksisso_n)

r2_p = r2_score(ktrue_p, ksisso_p)
rmse_p = np.sqrt(mean_squared_error(ktrue_p, ksisso_p))
mae_p = mean_absolute_error(ktrue_p, ksisso_p)

# 输出R^2、RMSE和MAE
print('PFn - R^2 = ' + str(r2_n))
print('PFn - RMSE = ' + str(rmse_n))
print('PFn - MAE = ' + str(mae_n))
print('PFp - R^2 = ' + str(r2_p))
print('PFp - RMSE = ' + str(rmse_p))
print('PFp - MAE = ' + str(mae_p))

# 计算误差
errors_n = np.abs(ktrue_n - ksisso_n)
errors_p = np.abs(ktrue_p - ksisso_p)

# 创建一个2x4的子图布局
fig, axs = plt.subplots(2, 4, figsize=(20, 10))

# 绘制PFn的图
axs[0, 0].scatter(ktrue_n, ksisso_n, c=errors_n, cmap='RdBu', vmin=errors_n.min(), vmax=errors_n.max(), alpha=0.8, s=14)
axs[0, 0].plot([-7, 0], [-7, 0], color='black', linestyle='--')
axs[0, 0].set_ylim(-7, 0)
axs[0, 0].set_xlim(-7, 0)
axs[0, 0].set_xlabel('log$(PF_n)_{DFT}$ - [$W/m/K^{2}$]', fontname='Microsoft YaHei', fontsize=13)
axs[0, 0].set_ylabel('log$(PF_n)_{SISSO}$ - [$W/m/K^{2}$]', fontname='Microsoft YaHei', fontsize=13)
axs[0, 0].set_title('(a) SISSO - $PF_n$', fontname='Microsoft YaHei', fontsize=13)
axs[0, 0].tick_params(axis='both', direction='in')
fig.colorbar(axs[0, 0].collections[0], ax=axs[0, 0], label='Error')

sns.kdeplot(x=descriptor_1_n, y=ktrue_n, fill=False, ax=axs[0, 1], cmap='RdBu_r', color='#d77071')
axs[0, 1].scatter(descriptor_1_n, ktrue_n, alpha=0.8, s=15, cmap='RdBu')
axs[0, 1].set_ylabel('log$(PF_n)_{DFT}$ - [$W/m/K^{2}$]', fontname='Microsoft YaHei', fontsize=13)
axs[0, 1].set_xlabel(
    r'$D_1 = {f_{\rm{p}}}N_{\rm{M}}^{\max }\left| {\Delta {{\bar r}_{{\rm{cov}}}} - N_{\rm{M}}^{\max }} \right|\left( {N_{\rm{U}}^{\max } + N_{{\rm{dU}}}^{\max }} \right)$',
    fontname='Microsoft YaHei', fontsize=13)
axs[0, 1].set_title(r'(b) log$(PF_n)_{DFT}$ ~ $D_1$', fontname='Microsoft YaHei', fontsize=13)
axs[0, 1].tick_params(axis='both', direction='in')

sns.kdeplot(x=descriptor_2_n, y=ktrue_n, fill=False, ax=axs[0, 2], cmap='RdBu_r', color='#d77071')
axs[0, 2].scatter(descriptor_2_n, ktrue_n, alpha=0.8, s=15, cmap='RdBu')
axs[0, 2].set_ylabel('log$(PF_n)_{DFT}$ - [$W/m/K^{2}$]', fontname='Microsoft YaHei', fontsize=13)
axs[0, 2].set_xlabel(
    r'$D_2 = \cos \left( {{{\left( {N_{{\rm{dU}}}^{\max }} \right)}^6}} \right)\left( {N_{\rm{U}}^{\max } - 2N_{{\rm{dU}}}^{\max }} \right)$',
    fontname='Microsoft YaHei', fontsize=13)
axs[0, 2].set_title(r'(c) log$(PF_n)_{DFT}$ ~ $D_2$', fontname='Microsoft YaHei', fontsize=13)
axs[0, 2].tick_params(axis='both', direction='in')

sns.kdeplot(x=descriptor_3_n, y=ktrue_n, fill=False, ax=axs[0, 3], cmap='RdBu_r', color='#d77071')
axs[0, 3].scatter(descriptor_3_n, ktrue_n, alpha=0.8, s=15, cmap='RdBu')
axs[0, 3].set_ylabel('log$(PF_n)_{DFT}$ - [$W/m/K^{2}$]', fontname='Microsoft YaHei', fontsize=13)
axs[0, 3].set_xlabel(
    r'$D_3 = {\left| {{E_{\rm{g}}} - N_{{\rm{dU}}}^{\max } - \sin \left( {\bar \chi } \right)\left( {N_{{\rm{dU}}}^{\max } - N_{\rm{U}}^{\max }} \right)} \right|}$',
    fontname='Microsoft YaHei', fontsize=13)
axs[0, 3].set_title(r'(d) log$(PF_n)_{DFT}$ ~ $D_3$', fontname='Microsoft YaHei', fontsize=13)
axs[0, 3].tick_params(axis='both', direction='in')

# 绘制PFp的图
axs[1, 0].scatter(ktrue_p, ksisso_p, c=errors_p, cmap='RdBu', vmin=errors_p.min(), vmax=errors_p.max(), alpha=0.8, s=14)
axs[1, 0].plot([-7, 0], [-7, 0], color='black', linestyle='--')
axs[1, 0].set_ylim(-7, 0)
axs[1, 0].set_xlim(-7, 0)
axs[1, 0].set_xlabel('log$(PF_p)_{DFT}$ - [$W/m/K^{2}$]', fontname='Microsoft YaHei', fontsize=13)
axs[1, 0].set_ylabel('log$(PF_p)_{SISSO}$ - [$W/m/K^{2}$]', fontname='Microsoft YaHei', fontsize=13)
axs[1, 0].set_title('(e) SISSO - $PF_p$', fontname='Microsoft YaHei', fontsize=13)
axs[1, 0].tick_params(axis='both', direction='in')
fig.colorbar(axs[1, 0].collections[0], ax=axs[1, 0], label='Error')

sns.kdeplot(x=descriptor_1_p, y=ktrue_p, fill=False, ax=axs[1, 1], cmap='RdBu_r', color='#d77071')
axs[1, 1].scatter(descriptor_1_p, ktrue_p, alpha=0.8, s=15, cmap='RdBu')
axs[1, 1].set_ylabel('log$(PF_p)_{DFT}$ - [$W/m/K^{2}$]', fontname='Microsoft YaHei', fontsize=13)
axs[1, 1].set_xlabel(
    r'$D_1 = {f_{\rm{p}}}N_{\rm{M}}^{\max }\left| {\Delta {{\bar r}_{{\rm{cov}}}} - N_{\rm{M}}^{\max }} \right|\left( {N_{\rm{U}}^{\max } + N_{{\rm{dU}}}^{\max }} \right)$',
    fontname='Microsoft YaHei', fontsize=13)
axs[1, 1].set_title(r'(f) log$(PF_p)_{DFT}$ ~ $D_1$', fontname='Microsoft YaHei', fontsize=13)
axs[1, 1].tick_params(axis='both', direction='in')

sns.kdeplot(x=descriptor_2_p, y=ktrue_p, fill=False, ax=axs[1, 2], cmap='RdBu_r', color='#d77071')
axs[1, 2].scatter(descriptor_2_p, ktrue_p, alpha=0.8, s=15, cmap='RdBu')
axs[1, 2].set_ylabel('log$(PF_p)_{DFT}$ - [$W/m/K^{2}$]', fontname='Microsoft YaHei', fontsize=13)
axs[1, 2].set_xlabel(
    r'$D_2 = \cos \left( {{{\left( {N_{{\rm{dU}}}^{\max }} \right)}^6}} \right)\left( {N_{\rm{U}}^{\max } - 2N_{{\rm{dU}}}^{\max }} \right)$',
    fontname='Microsoft YaHei', fontsize=13)
axs[1, 2].set_title(r'(g) log$(PF_p)_{DFT}$ ~ $D_2$', fontname='Microsoft YaHei', fontsize=13)
axs[1, 2].tick_params(axis='both', direction='in')

sns.kdeplot(x=descriptor_3_p, y=ktrue_p, fill=False, ax=axs[1, 3], cmap='RdBu_r', color='#d77071')
axs[1, 3].scatter(descriptor_3_p, ktrue_p, alpha=0.8, s=15, cmap='RdBu')
axs[1, 3].set_ylabel('log$(PF_p)_{DFT}$ - [$W/m/K^{2}$]', fontname='Microsoft YaHei', fontsize=13)
axs[1, 3].set_xlabel(
    r'$D_3 = {\left| {{E_{\rm{g}}} - N_{{\rm{dU}}}^{\max } - \sin \left( {\bar \chi } \right)\left( {N_{{\rm{dU}}}^{\max } - N_{\rm{U}}^{\max }} \right)} \right|}$',
    fontname='Microsoft YaHei', fontsize=13)
axs[1, 3].set_title(r'(h) log$(PF_p)_{DFT}$ ~ $D_3$', fontname='Microsoft YaHei', fontsize=13)
axs[1, 3].tick_params(axis='both', direction='in')

# 设置每个子图的边框宽度为 2
for ax in axs.flatten():
    for spine in ax.spines.values():
        spine.set_linewidth(2)

plt.tight_layout()
plt.show()
