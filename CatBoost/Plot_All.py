import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']

target = ['PF_n', 'PF_p']
for tg in target:
    train_file_name = f'{tg}_train_results.csv'
    test_file_name = f'{tg}_results.csv'

    train_data = pd.read_csv(train_file_name)
    test_data = pd.read_csv(test_file_name)

    train_targets = train_data['True Value']
    train_features = train_data['Predicted Value']
    test_targets = test_data['True Value']
    test_features = test_data['Predicted Value']

    train_mae = mean_absolute_error(train_targets, train_features)
    train_r2 = r2_score(train_targets, train_features)

    test_mae = mean_absolute_error(test_targets, test_features)
    test_r2 = r2_score(test_targets, test_features)

    fig, ax = plt.subplots(figsize=(10, 8))

    ax.scatter(train_features, train_targets, label='Train', color='#2256F2', alpha=0.8, s=15)
    ax.scatter(test_features, test_targets, label='Test', color='#D9184B', alpha=0.8, s=15)

    ax.set_xlabel('DFT Calculation', fontsize=16, fontname='Times New Roman')
    ax.set_ylabel('ML Prediction', fontsize=16, fontname='Times New Roman')

    x_min = -7
    x_max = 0
    y_min = -7
    y_max = 0

    ax.plot([x_min, x_max], [y_min, y_max], linestyle='dashed', color='black', clip_on=False)

    ax.text(0.05, 0.80, f'Train MAE: {train_mae:.3f}', transform=ax.transAxes, fontsize=16,
            fontname='Times New Roman')
    ax.text(0.05, 0.75, f'Train R-squared: {train_r2:.3f}', transform=ax.transAxes, fontsize=16,
            fontname='Times New Roman')
    ax.text(0.05, 0.7, f'Test MAE: {test_mae:.3f}', transform=ax.transAxes, fontsize=16,
            fontname='Times New Roman')
    ax.text(0.05, 0.65, f'Test R-squared: {test_r2:.3f}', transform=ax.transAxes, fontsize=16,
            fontname='Times New Roman')

    ax.legend(fontsize=16)
    tg = str(tg)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.tick_params(axis='both', direction='in', labelsize=16)
    # plt.title(f'ML vs DFT, log(${tg}$×10$^7$)', fontsize=16, fontname='Times New Roman')
    plt.tight_layout()

    plt.savefig(rf'MLvsDFT_{tg}.svg', dpi=200, bbox_inches='tight')
    plt.show()