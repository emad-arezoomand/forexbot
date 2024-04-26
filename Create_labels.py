import numpy as np

def multi_distance_labele_creator (data, min_distance, max_distance, num_labels):
    datalen = len(data)
    lim = np.linspace(min_distance,max_distance,num_labels)
    print("lims = \n",lim)
    labels = np.zeros((datalen,2*num_labels))
    for i,di in data.iterrows():
        closeprice = di['close']
        target_pending = [True for i in range(num_labels)]
        for j,dj in data.iloc[i+1:].iterrows():
            high = dj['high']
            low  = dj['low']
            for k,lk in enumerate(lim[target_pending]):
                k = target_pending.index(True)
                if high >= closeprice+lk :
                    labels[i,k] = 1
                    target_pending[k]=False
                if low <= closeprice-lk:
                    labels[i,k+num_labels] = 1
                    target_pending[k]=False
                if True in target_pending:
                    continue
                else :
                    break

    return labels

