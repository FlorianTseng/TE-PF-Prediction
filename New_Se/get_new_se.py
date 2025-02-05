import pandas as pd
from mp_api.client import MPRester
import os

api_key = "e0Ph5shLuV1N7NZLiyuSkiXgh2npOyyY"

mpr = MPRester(api_key)
data = []
crys_sys = ['Triclinic', 'Monoclinic', 'Orthorhombic', 'Tetragonal', 'Trigonal', 'Hexagonal', 'Cubic']
crys_sys_mapping = {
    'Triclinic': 1,
    'Monoclinic': 2,
    'Orthorhombic': 3,
    'Tetragonal': 4,
    'Trigonal': 5,
    'Hexagonal': 6,
    'Cubic': 7
}
for cs in crys_sys:
    for sgn in range(1, 231):
        results = mpr.materials.summary.search(
            fields=['formula_pretty', 'material_id', 'energy_above_hull', 'formation_energy_per_atom', 'band_gap',
                    'nsites', 'nelements'],
            spacegroup_number=sgn, crystal_system=cs, elements=['Se', 'Te'], num_sites=[1, 10], num_elements=[2, 10],
            band_gap=[0.00001, 1.4999999])

        for r in results:
            # print(r)
            id = r.material_id
            formula = r.formula_pretty
            nsites = r.nsites
            # print(nsites)
            eah = r.energy_above_hull
            # print(eah)
            fe = r.formation_energy_per_atom
            sg_n = sgn
            bg = r.band_gap
            ne = r.nelements
            data.append([id, formula, nsites, crys_sys_mapping[cs], eah, bg, fe, sg_n, ne])
            # print(data)

df = pd.DataFrame(data, columns=['mpid', 'formula', 'num_sites', 'crystal_system', 'e_hull', 'band_gap', 'formation',
                                 'space_group', 'num_elements'])
print(df)
df.to_csv('New_Se&Te.csv', mode='a', index=False, header=not os.path.exists(f'New_Se&Te.csv'))
