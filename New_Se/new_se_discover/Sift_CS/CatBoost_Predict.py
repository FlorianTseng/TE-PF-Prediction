import pandas as pd
import pickle

model_n_path = 'PF_n_model.pkl'
model_p_path = 'PF_p_model.pkl'
data_path = 'New_Se&Te_by_hand.csv'
output_path = 'predictions_sifted.csv'

with open(model_n_path, 'rb') as f:
    model1 = pickle.load(f)

with open(model_p_path, 'rb') as f:
    model2 = pickle.load(f)

data = pd.read_csv(data_path)
data_subset = data.iloc[:, :3]

predictions1 = model1.predict(data.iloc[:, 3:])
predictions2 = model2.predict(data.iloc[:, 3:])

output_data = pd.DataFrame({
    'mpid': data_subset.iloc[:, 0],
    'formula': data_subset.iloc[:, 1],
    'PFn Predictions': predictions1,
    'PFp Predictions': predictions2,
    'PF mean': (predictions1 + predictions2) / 2
})

output_data.to_csv(output_path, index=False)
