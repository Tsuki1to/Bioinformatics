# 开发时间：2022/11/18 15:33
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',400)
df1_0 = pd.read_csv('./adm_data.csv',index_col='Serial No.')
'''
GRE Scores ( out of 340 )
TOEFL Scores ( out of 120 )
University Rating ( out of 5 )
Statement of Purpose (SOP) and Letter of Recommendation (LOR) Strength ( out of 5 )
Undergraduate GPA ( out of 10 )
Research Experience ( either 0 or 1 )
Chance of Admit ( ranging from 0 to 1 ).
'''
# print(df1_0.head())
# print(df1_0.info())
# print(df1_0.describe())
df1 = df1_0.copy()
print(df1_0)
df1.drop(columns=['Chance of Admit '])

def norm_(x):
    xmean = np.mean(x,0)
    std = np.std(x,0)
    return (x-xmean)/std
df1 = norm_(df1)
print(df1.describe())
ew,ev = np.linalg.eig(np.cov(df1.T))
ew_order = np.argsort(ew)[::-1]
ew_sort = ew[ew_order]
ev_sort = ev[:,ew_order]
print(ew_sort)
#[5.68766116 0.7301124  0.55895302 0.32633295 0.2514573  0.19862308 0.15167516 0.11523505]
print(ev_sort)
pd.DataFrame(ew_sort).plot(kind = 'bar')
plt.show()
V= ev_sort[:,:2]
X_new = df1.dot(V)
sc = plt.scatter(X_new.iloc[:,0],X_new.iloc[:,1],s=5,c= df1_0['Chance of Admit '],cmap= plt.cm.coolwarm)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.colorbar(sc)
print(V)
print(df1.columns)
plt.show()