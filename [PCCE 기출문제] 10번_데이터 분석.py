import pandas as pd

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = 'date'
val_ext = 20300501
sort_by = 'remain'

data = pd.DataFrame(data, columns=['code', 'date', 'maximum', 'remain'])
answer_data = data.loc[data[ext] < val_ext].sort_values(by=sort_by)
answer = [list(i.values()) for i in answer_data.to_dict('records')]
print(answer)
