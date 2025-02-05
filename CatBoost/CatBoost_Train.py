import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import catboost as cb
import optuna
import joblib

# 读取六个特征的数据集
feature_files = ['csPF_n.csv']
target_names = ['PF_n']
best_params_dict = {}  # 保存每个目标的最佳参数

for target_name, feature_file in zip(target_names, feature_files):
    data = pd.read_csv(feature_file)
    features = data.iloc[:, 2:].values
    target = data.iloc[:, 1].values
    sample_names = data.iloc[:, 0].values

    X_train, X_val, y_train, y_val, names_train, names_val = train_test_split(features, target, sample_names,
                                                                              test_size=0.1, random_state=24)

    def objective(trial):
        params = {
            'iterations': trial.suggest_int('iterations', 50, 500),
            'learning_rate': trial.suggest_float('learning_rate', 0.0001, 0.5),
            'depth': trial.suggest_int('depth', 4, 10),
            'subsample': trial.suggest_float('subsample', 0.8, 1),
            'colsample_bylevel': trial.suggest_float('colsample_bylevel', 0.8, 1),
            'l2_leaf_reg': trial.suggest_float('l2_leaf_reg', 0.5, 50),
        }

        catboost_model = cb.CatBoostRegressor(**params, verbose=0)

        catboost_model.fit(X_train, y_train)

        y_pred = catboost_model.predict(X_val)

        r2 = r2_score(y_val, y_pred)

        return r2

    study = optuna.create_study(direction='maximize')
    study.optimize(objective, n_trials=200)

    best_params = study.best_params
    best_params_dict[target_name] = best_params

    print("Best Params for", target_name, ":", best_params)

    catboost_model = cb.CatBoostRegressor(**best_params, verbose=0)
    catboost_model.fit(X_train, y_train)

    y_train_pred = catboost_model.predict(X_train)
    r2_train = r2_score(y_train, y_train_pred)
    mae_train = mean_absolute_error(y_train, y_train_pred)

    y_val_pred = catboost_model.predict(X_val)
    r2_val = r2_score(y_val, y_val_pred)
    mae_val = mean_absolute_error(y_val, y_val_pred)

    print("R^2 on Train Set for", target_name, ":", r2_train)
    print("MAE on Train Set for", target_name, ":", mae_train)
    print("R^2 on Test Set for", target_name, ":", r2_val)
    print("MAE on Test Set for", target_name, ":", mae_val)

    results_df = pd.DataFrame({'Sample Name': names_val, 'True Value': y_val, 'Predicted Value': y_val_pred})
    results_df.to_csv(f'{target_name}_results.csv', header=True, index=False)

    train_results_df = pd.DataFrame(
        {'Sample Name': names_train, 'True Value': y_train, 'Predicted Value': y_train_pred})
    train_results_df.to_csv(f'{target_name}_train_results.csv', header=True, index=False)

    # 保存最佳模型
    joblib.dump(catboost_model, f"{target_name}_model.pkl")

with open('best_params.txt', 'w') as f:
    for target_name, params in best_params_dict.items():
        f.write(f"Target: {target_name}\n")
        f.write(f"Best Params: {params}\n")
        f.write("\n")
