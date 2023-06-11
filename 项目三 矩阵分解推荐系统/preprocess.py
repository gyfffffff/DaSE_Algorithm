# 将数据处理成用户-商品矩阵
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

rawdata = pd.read_csv('ml-latest-small/ratings.csv')
le = LabelEncoder()
rawdata['movieId_ec'] = le.fit_transform(rawdata['movieId'])
rawdata = rawdata.drop(columns=['movieId','timestamp'])

rawdata_ndarray = rawdata.values  # 得到numpy矩阵
n = rawdata_ndarray.shape[0]

usrlist = rawdata['userId'].astype(int)
movielist = rawdata['movieId_ec'].astype(int)
un = len(set(usrlist))
mn = len(set(movielist))

UIMatrix = np.zeros((un+1,mn+1)).astype(int)
for i in range(n):
    u = int(rawdata_ndarray[i, 0])
    m = int(rawdata_ndarray[i, 2])
    r = int(rawdata_ndarray[i, 1])
    UIMatrix[u, m] = r
np.save('UIMatrix', UIMatrix)

