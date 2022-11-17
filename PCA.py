# 开发时间：2022/11/16 14:45
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)



file_path = './train.csv'
df_0 = pd.read_csv(file_path)
# # print(df_0.info())
# # print(df_0.head(10))
# '''数据整理'''
# df = df_0.copy()
# #数据替换
# df.Sex = df.Sex.replace({'female':0,'male':1})
# df.Embarked = df.Embarked.replace({'C':0,'Q':1,'S':2})  #one  hot
# #填充Nan
# df.Age.fillna(df.Age.mean(),inplace = True)
# df.Embarked.fillna(method='ffill',inplace = True)
# #fillna中ffill的意思是按照前面的数据进行填充front fill nan 向前填充or向下填充
# #相对应bfill就是按照后面的数据进行填充    向后填充or向上填充
# #舍弃不需要的数据
# df.drop(columns=['Survived','Name','Ticket','Cabin'],inplace=True)
# df.to_csv('titanic_data_pure_PCA.csv',index=False)
# print(df.info())


df1 = pd.read_csv('titanic_data_pure_PCA.csv',index_col='PassengerId')
df1.drop(labels='Unnamed: 0',axis=1,inplace=True)

# print(df1.head())
# print(df1.describe())
#normalization 去均值，标准化（去中心化）
def norm_(x):
    xmean = np.mean(x,0)
    std = np.std(x,0)
    return (x-xmean)/std
df1_ = norm_(df1)
print(df1_.describe())
#V
#np.linalg.eig()  求矩阵的特征值与特征向量
# ew,ev = np.linalg.eig(df1_.T.dot(df1_))   #x.T.dot(矩阵内积)x   ==cov(x.T) 上下两个公式得出的特征值有差别
ew,ev = np.linalg.eig(np.cov(df1_.T))
  #7个feature对应7个特征值
#ew特征值的排序
ew_order = np.argsort(ew)[::-1]
ew_sort = ew[ew_order]
ev_sort = ev[:,ew_order]
print(ew_sort)  #得到的特征值及方差
print(ev_sort)
# 取K值，及前K个标准差的和大于全部和95%
#将取值前7个feature数据降维到K个feature
#使用前K个数据近似的代表原先的7组数据的结果
pd.DataFrame(ew_sort).plot(kind = 'bar')
plt.show()

#ev_sort--->V
V = ev_sort[:,:2]
#X_new
X_new = df1_.dot(V)
# print(X_new.shape) #(891, 2)   #由原先的7列数据降维到了2列数据
#scatter
sc = plt.scatter(X_new.iloc[:,0],X_new.iloc[:,1],s=5,c =df_0.Survived,cmap=plt.cm.coolwarm)
plt.xlabel('PC0')
plt.ylabel('PC1')
plt.colorbar(sc)
print(V)
print(df1_.columns)

plt.show()
