# 开发时间：2022/11/15 14:46
import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)
f = open('./CYP90D1.fasta')
a = f.readlines()

f.close()

sequences = {}
for i in a:
    if('>' in i):
        key_temp = i[1:].strip()
        print(key_temp)
    else:
        sequences[key_temp] = i.strip()

print(sequences)

# seq= []
# for i in range(0,len(a)):
# # print(i)
#     if('>' in a[i]):
#         if(i!= 0):
#             key_temp = a[i][1:].strip()
#             sequences[key_temp] = ''.join(seq)
#             print(key_temp)
#             seq=[]
#         else:
#             seq.append(a[i].strip())
# print(sequences)
