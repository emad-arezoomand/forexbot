import numpy as np

def create_window_indexes (len_data,len_window):
    indexes = []
    dif = len_data-len_window + 1
    s = 0 ; e = len_window
    for i in range(dif):
        r = np.arange(s,e)
        indexes.append(r)
        s +=1 ; e += 1
    return np.array(indexes)

def apply_windower_to_series_data(data, labels,windows_indexes):
    dataset = []
    for i in range(len(windows_indexes)):
        chunk_data = data.iloc[windows_indexes[i]]
        associated_label = labels[[windows_indexes[i][-1]]]
        dataset.append((chunk_data,associated_label))
    return dataset