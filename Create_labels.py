import numpy as np

def multi_distance_label_creator (data, min_distance, max_distance, num_labels):
    datalen = len(data)
    lim = np.linspace(min_distance,max_distance,num_labels)
    print("lims = \n",lim)
    labels = np.zeros((datalen,2*num_labels))
    for i_ in range(len(data)):
        di = data.iloc[i_]
        closeprice = di['close']
        target_pending = [True for _ in range(num_labels)]
        # print()
        # print("at close price and date = ",closeprice , di['date'])
        for j_ in range(len(data.iloc[i_+1:])):
            dj = data.iloc[i_+1+j_]
            high = dj['high']
            low  = dj['low']
            # print("secondary at date = ", dj['date'])
            for k,lk in enumerate(lim[target_pending]):
                kid = target_pending.index(True)
                if high >= closeprice+lk :
                    labels[i_,kid] = 1
                    target_pending[kid]=False
                if low <= closeprice-lk:
                    labels[i_,kid+num_labels] = 1
                    target_pending[kid]=False
                if True in target_pending:
                    continue
                else :
                    break
            # print("labels filled until now = ", labels[::i_])
            if True in target_pending:
                continue
            else :
                break
    return labels

# def multi_distance_label_creator_1 (data, min_distance, max_distance, num_labels):
#     datalen = len(data)
#     lim = np.linspace(min_distance,max_distance,num_labels)
#     print("lims = \n",lim)
#     labels = np.zeros((datalen,2*num_labels))
#     for i,di in data.iterrows():
#         closeprice = di['close']
#         target_pending = [True for i in range(num_labels)]
#         for j,dj in data.iloc[i+1:].iterrows():
#             high = dj['high']
#             low  = dj['low']
#             for k,lk in enumerate(lim[target_pending]):
#                 k = target_pending.index(True)
#                 if high >= closeprice+lk :
#                     labels[i,k] = 1
#                     target_pending[k]=False
#                 if low <= closeprice-lk:
#                     labels[i,k+num_labels] = 1
#                     target_pending[k]=False
#                 if True in target_pending:
#                     continue
#                 else :
#                     break
#
#     return labels