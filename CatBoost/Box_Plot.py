import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "Microsoft YaHei"
plt.rcParams["font.size"] = 16

crys_sys = ['Triclinic', 'Monoclinic', 'Orthorhombic', 'Tetragonal', 'Trigonal', 'Hexagonal', 'Cubic']

targets = ['PF_n', 'PF_p']
colormap = 'RdBu_r'  # 设置颜色映射

fig, axes = plt.subplots(2, 1, figsize=(12, 12))

for i, tg in zip(range(2), targets):
    true_values = []
    predicted_values = []
    sample_sizes = []
    for cs in crys_sys:
        train_csv_file = f"{cs}_results/{cs}_{tg}_train.csv"
        test_csv_file = f"{cs}_results/{cs}_{tg}.csv"

        train_data = pd.read_csv(train_csv_file)
        test_data = pd.read_csv(test_csv_file)

        true_values.append(train_data["True Value"].tolist() + test_data["True Value"].tolist())
        predicted_values.append(train_data["Predicted Value"].tolist() + test_data["Predicted Value"].tolist())
        sample_sizes.append(len(train_data) + len(test_data))

    ax1 = axes[i]
    bp = ax1.boxplot(true_values, patch_artist=True)

    # 设置每个箱线图的颜色
    cmap = plt.cm.get_cmap(colormap)
    for patch, color_index in zip(bp['boxes'], np.linspace(0, 1, len(crys_sys))):
        patch.set_facecolor(cmap(color_index))

    plt.setp(bp['medians'], color='black')  # 将中位线颜色设置为黑色
    ax1.set_title(f"({chr(97+i)}) Box Plot of DFT Calculated ${tg}$", fontname="Microsoft YaHei", fontsize=15)
    ax1.set_ylabel("DFT Calculated Value", fontname="Microsoft YaHei", fontsize=15)
    if i < 1:  # 隐藏上侧图的横坐标标签和刻度
        ax1.set_xticklabels([])
        ax1.set_xticks([])
    else:
        # ax1.set_xlabel("Crystal System", fontname="Microsoft YaHei", fontsize=15)
        ax1.set_xticks(range(1, len(crys_sys) + 1))
        ax1.set_xticklabels(crys_sys, rotation=45, fontname="Microsoft YaHei", fontsize=15)
    ax1.tick_params(axis="both", direction="in")

    ax2 = ax1.twinx()
    ax2.plot(np.arange(1, len(crys_sys) + 1), sample_sizes, color='#8C1E14', marker='o')
    ax2.set_ylabel("Sample Size", color='#8C1E14', fontname="Microsoft YaHei", fontsize=15)
    ax2.tick_params(axis="y", colors='#8C1E14', direction="in")  # Change the direction of tick labels to inward

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 1, figsize=(12, 12))

for i, tg in zip(range(2), targets):
    true_values = []
    predicted_values = []
    sample_sizes = []
    for cs in crys_sys:
        train_csv_file = f"{cs}_results/{cs}_{tg}_train.csv"
        test_csv_file = f"{cs}_results/{cs}_{tg}.csv"

        train_data = pd.read_csv(train_csv_file)
        test_data = pd.read_csv(test_csv_file)

        true_values.append(train_data["True Value"].tolist() + test_data["True Value"].tolist())
        predicted_values.append(train_data["Predicted Value"].tolist() + test_data["Predicted Value"].tolist())
        sample_sizes.append(len(train_data) + len(test_data))

    ax1 = axes[i]
    bp = ax1.boxplot(predicted_values, patch_artist=True)

    # 设置每个箱线图的颜色
    cmap = plt.cm.get_cmap(colormap)
    for patch, color_index in zip(bp['boxes'], np.linspace(0, 1, len(crys_sys))):
        patch.set_facecolor(cmap(color_index))

    plt.setp(bp['medians'], color='black')  # 将中位线颜色设置为黑色
    ax1.set_title(f"Box Plot of ML(XGB) Predicted {tg}", fontname="Microsoft YaHei", fontsize=15)
    ax1.set_ylabel("ML Predicted Value", fontname="Microsoft YaHei", fontsize=15)
    if i < 1:  # 隐藏上侧图的横坐标标签和刻度
        ax1.set_xticklabels([])
        ax1.set_xticks([])
    else:
        ax1.set_xlabel("Crystal System", fontname="Microsoft YaHei", fontsize=15)
        ax1.set_xticks(range(1, len(crys_sys) + 1))
        ax1.set_xticklabels(crys_sys, rotation=45, fontname="Microsoft YaHei", fontsize=15)
    ax1.tick_params(axis="both", direction="in")

    ax2 = ax1.twinx()
    ax2.plot(np.arange(1, len(crys_sys) + 1), sample_sizes, color='#8C1E14', marker='o')
    ax2.set_ylabel("Sample Size", color='#8C1E14', fontname="Microsoft YaHei", fontsize=16)
    ax2.tick_params(axis="y", colors='#8C1E14', direction="in")  # Change the direction of tick labels to inward

plt.tight_layout()
plt.show()
