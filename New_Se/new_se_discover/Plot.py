import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

df_sifted = pd.read_csv('predictions_sifted.csv')
df_unsifted = pd.read_csv('predictions_unsifted.csv')

columns = ['PFn Predictions', 'PFp Predictions', 'PF mean']

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

for i, column in enumerate(columns):
    axs[i].scatter(df_unsifted[column], df_sifted[column], color='#D9184B', alpha=0.8, s=15)
    axs[i].set_xlabel('$m_B$ Prediction')
    axs[i].set_ylabel('$m_{Eq}$ Prediction')
    axs[i].set_xlim(-7, 0)
    axs[i].set_ylim(-7, 0)
    axs[i].set_aspect('equal')

    r2 = r2_score(df_sifted[column], df_unsifted[column])
    if i < 2:
        axs[i].set_title(f'${column}$ (R-squared = {r2:.2f})')
    else:
        axs[i].set_title('$PF_{mean}$' + f' (R-squared = {r2:.2f})')
    # 设置刻度线朝内
    axs[i].tick_params(direction='in')

    # 添加黑色虚线
    axs[i].plot([-7, 0], [-7, 0], color='black', linestyle='dashed')

plt.tight_layout()
plt.show()
