import pandas as pd
from mp_api.client import MPRester
import os

api_key = "e0Ph5shLuV1N7NZLiyuSkiXgh2npOyyY"

mpr = MPRester(api_key)
data = []
file = pd.read_csv("New_Te&Se_unique.csv")
mpids = file['mpid'].tolist()

# 将所有mpids转换为字符串
mpids = [str(mpid) for mpid in mpids]

# 将mpids转换为字符串，每个ID用逗号分隔
mpids_str = ','.join(mpids)

results = mpr.materials.summary.search(
    fields=['formula_pretty', 'material_id', 'energy_above_hull', 'formation_energy_per_atom', 'band_gap', 'nsites'],
    material_ids=mpids_str
)

for r in results:
    print(r)
    id = r.material_id
    formula = r.formula_pretty
    nsites = r.nsites
    eah = r.energy_above_hull
    fe = r.formation_energy_per_atom
    bg = r.band_gap
    data.append([id, formula, nsites, eah, bg, fe])

df = pd.DataFrame(data, columns=['mpid', 'formula', 'num_sites', 'e_hull', 'band_gap', 'formation'])
print(df)
df.to_csv('Se&Te_by_hand.csv', mode='a', index=False, header=not os.path.exists('Se&Te_by_hand.csv'))
