# 开发时间：2022/11/15 14:46
import pandas as pd
from Bio.SeqUtils import GC
from Bio import SeqIO as SI

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)
'''BioPyhton方法'''
sequence = {}
for i in SI.parse('CYP90D1.fasta','fasta'):
    # print(i.id)
    # print(i.seq)
    # print('基因ID为:',i.id,'\n','基因序列为：',i.seq,'基因的序列长度为：',len(i.seq),'基因的GC含量为：',GC((i.seq)))
    sequence[(i.id)] = str(i.seq)

a = pd.Series(sequence,index=[1,2,3])
print(a)
# b= pd.DataFrame(a,index=a.index,columns=[1,2,3])













'''传统格式'''
# f = open('./CYP90D1.fasta')
# a = f.readlines()
#
# f.close()

# sequences = {}
# for i in a:
#     # print(i)
#     if('>' in i):
#         key_temp = i[10].strip()
#         print(key_temp)
#     else:
#         sequences[key_temp] = i.strip()
#
# print(sequences)

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
