import pandas as pd
import joblib

loaded_models = {}
target_names = ['PF_n', 'PF_p']

for target_name in target_names:
    loaded_models[target_name] = joblib.load(f"{target_name}_model.pkl")

    new_sample_file = 'new_sample.csv'
    new_sample_data = pd.read_csv(new_sample_file)

    new_sample_features = new_sample_data.iloc[:, 1:].values
    new_sample_names = new_sample_data.iloc[:, 0]

    predictions = {}

    for target_name, model in loaded_models.items():
        predictions[target_name] = model.predict(new_sample_features)

    for target_name, prediction in predictions.items():
        print(f"Predictions for log({target_name}*10^9):")
        for name, pred in zip(new_sample_names, prediction):
            print(f"{name}: {pred}")
