import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from matplotlib import rcParams
import seaborn as sns

# 设置字体为微软雅黑
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 读取数据
data = np.genfromtxt('desc_D003_t001.dat', skip_header=1, usecols=(1, 2, 3, 4, 5))

# 提取真实值和预测值
ktrue = data[:, 0]
ksisso = data[:, 1]
descriptor_1 = data[:, 2]
descriptor_2 = data[:, 3]
descriptor_3 = data[:, 4]

# 计算R^2、RMSE和MAE
r2 = r2_score(ktrue, ksisso)
rmse = np.sqrt(mean_squared_error(ktrue, ksisso))
mae = mean_absolute_error(ktrue, ksisso)

# 输出R^2、RMSE和MAE
print('R^2 = ' + str(r2))
print('RMSE = ' + str(rmse))
print('MAE = ' + str(mae))

# 计算误差
errors = np.abs(ktrue - ksisso)

# 创建一个正方形画布
fig = plt.figure(figsize=(10, 10))

# 绘制第一幅图
ax1 = plt.subplot(2, 2, 1)
scatter = ax1.scatter(ktrue, ksisso, c=errors, cmap='RdBu', vmin=errors.min(), vmax=errors.max(), alpha=0.8, s=14)
plt.colorbar(scatter, label='Error')  # 添加颜色条
plt.xlim(-7, 0)
plt.ylim(-7, 0)
plt.xlabel('log$(PF_p)_{DFT}$ - [$W/m^2 K^{-1}$]', fontname='Microsoft YaHei', fontsize=15)
plt.ylabel('log$(PF_p)_{SISSO}$ - [$W/m^2 K^{-1}$]', fontname='Microsoft YaHei', fontsize=15)
plt.title('(e) SISSO - $PF_p$', fontname='Microsoft YaHei', fontsize=15)
plt.tick_params(axis='both', direction='in')
plt.plot([-7, 0], [-7, 0], color='black', linestyle='--')

# 绘制第二幅图
ax2 = plt.subplot(2, 2, 2)
sns.kdeplot(x=descriptor_1, y=ktrue, fill=False, ax=ax2, cmap='RdBu_r')
plt.scatter(descriptor_1, ktrue, cmap='RdBu', alpha=0.8, s=15)
plt.ylabel('log$(PF_p)_{DFT}$ - [$W/m^2 K^{-1}$]', fontname='Microsoft YaHei', fontsize=15)
plt.xlabel(
    r'$D_1 = {f_{\rm{p}}}{\chi ^{\max }}\left[ {\frac{1}{{\pi \left( {1 + S{G^2}} \right)}} + \frac{1}{{\pi \left( {1 + \bar N_{{\rm{dU}}}^2} \right)}}} \right]$',
    fontname='Microsoft YaHei', fontsize=15)
plt.title(r'(f) log$(PF_p)_{DFT}$ ~ $D_1$', fontname='Microsoft YaHei', fontsize=15)
plt.tick_params(axis='both', direction='in')

# 绘制第三幅图
ax3 = plt.subplot(2, 2, 3)
sns.kdeplot(x=descriptor_2, y=ktrue, fill=False, ax=ax3, cmap='RdBu_r')
plt.scatter(descriptor_2, ktrue, cmap='RdBu', alpha=0.8, s=15)
plt.ylabel('log$(PF_p)_{DFT}$ - [$W/m^2 K^{-1}$]', fontname='Microsoft YaHei', fontsize=15)
plt.xlabel(
    r'$D_2 = \frac{{{\chi ^{\max }}}}{{\sqrt[3]{{\bar N}}}}\cos \left( {\frac{{{{\bar N}_{\rm{U}}}}}{{{\chi ^{\max }}}}} \right)$',
    fontname='Microsoft YaHei', fontsize=15)
plt.title(r'(g) log$(PF_p)_{DFT}$ ~ $D_2$', fontname='Microsoft YaHei', fontsize=15)
plt.tick_params(axis='both', direction='in')

# 绘制第四幅图
ax4 = plt.subplot(2, 2, 4)
sns.kdeplot(x=descriptor_3, y=ktrue, fill=False, ax=ax4, cmap='RdBu_r')
plt.scatter(descriptor_3, ktrue, cmap='RdBu', alpha=0.8, s=15)
plt.ylabel('log$(PF_p)_{DFT}$ - [$W/m^2 K^{-1}$]', fontname='Microsoft YaHei', fontsize=15)
plt.xlabel(
    r'$D_3 = \log \left( {{{\bar T}_{\rm{M}}}SG} \right)\exp \left( {\frac{{{f_{\rm{p}}}}}{{{\chi ^{\max }}}}} \right)$',
    fontname='Microsoft YaHei', fontsize=15)
plt.title(r'(h) log$(PF_p)_{DFT}$ ~ $D_3$', fontname='Microsoft YaHei', fontsize=15)
plt.tick_params(axis='both', direction='in')

# 调整子图之间的间距
plt.tight_layout()

plt.show()
