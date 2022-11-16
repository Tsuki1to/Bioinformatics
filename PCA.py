# 开发时间：2022/11/16 14:45
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# pd.set_option('display.max_rows',None)
# pd.set_option('display.max_columns',None)
# pd.set_option('max_colwidth',300)



# file_path = './train.csv'
# df_0 = pd.read_csv(file_path)
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
print(df1.head())
print(df1.describe())