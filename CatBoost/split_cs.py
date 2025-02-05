import os
import pandas as pd
from mp_api.client import MPRester

api_key = "e0Ph5shLuV1N7NZLiyuSkiXgh2npOyyY"

mpr = MPRester(api_key)
targets = ['PF_n', 'PF_p']
part = ['_train', '']

for pt in part:
    for tg in targets:
        csv_file = f"{tg}{pt}_results.csv"
        df = pd.read_csv(csv_file)
        mpid = df["Sample Name"].tolist()

        crys_sys = ['Triclinic', 'Monoclinic', 'Orthorhombic', 'Tetragonal', 'Trigonal', 'Hexagonal', 'Cubic']

        for cs in crys_sys:
            folder_path = f"{cs}_results"
            os.makedirs(folder_path, exist_ok=True)

        for cs in crys_sys:
            results = mpr.summary.search(material_ids=mpid, fields=["material_id"], crystal_system=cs)

            if not results:
                print(f"{cs} is empty.")
            else:
                csv_filename = f"{cs}_results/{cs}_{tg}{pt}.csv"
                mpid_list = [r.material_id for r in results]
                selected_columns = ["Sample Name"] + df.columns[1:].tolist()
                selected_df = df[df["Sample Name"].isin(mpid_list)]
                selected_df = selected_df[selected_columns]
                selected_df.to_csv(csv_filename, index=False)

                print(f"{cs}_{tg} successfully saved!")
