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

