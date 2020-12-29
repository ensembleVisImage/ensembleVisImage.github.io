import pandas as pd
import numpy as np

target_papers = "ensemble_papers.csv"
all_papers = "vispubData30.csv"
filtered_papers = "new_vispubData30.csv"

target = pd.read_csv(target_papers)
all = pd.read_csv(all_papers)
target_doi = np.array(target['link'], dtype='str')
all_doi = np.array(all['paper_url'], dtype='str')

drop_list = []
for i, doi in enumerate(all_doi):
    if doi not in target_doi:
        drop_list.append(i)

filtered = all.drop(drop_list)
filtered.to_csv(filtered_papers)
