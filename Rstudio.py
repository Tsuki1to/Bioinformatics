# 开发时间：2023/1/3/0003 下午 04:17
import math
x = (1,2,3,4)
print(x)
z = ()
#在x向量集中，5的后面添加值99

# > append(x=v,values= 99, after = 5)
# #after = 0，则在向量的开头插入数据
# > append(x=v,values= 99, after = 0)

'''向量的运算'''
#seq（1,100，length.out = 10）生成等差数列length.out = 10，输出为10个数字的向量集
'''
x**y   为乘幂运算
x%%y   为求余运算
x%/%y   为整除运算
如果两个长度不相同的向量集进行运算，短的向量循环使用，长的向量集必须是短的向量集的整数倍
abs(x)返回向量的绝对值
sqrt(x)计算平方根
log(16,base = 2)计算log16以2位底的对数
log10(x)log以10为底的x的对数
exp(x)计算向量x中每个函数的指数
ceiling(x)在向量x中每个函数向上取整
floor(x)在向量x中每个函数向下取整
trunc(x)向量x中只取整数部分
round(x,digits = 2)函数进行四舍五入，digits = 2表示保留小数点后两位
signif(x,digits = 3)保留向量集x中的
sum(x)求和
max(x)求最大值
min(x)求最小值
range(x)直接返回最大值和最小值
mean(x)均值
var(x)返回向量的方差
sd(x)返回向量的标准差
prod(x)返回向量x连乘的积
median(x)计算中位数
quantile(x)计算分位数
quantile(x,c(0.4,0.5,0.8))计算40%，50%，80%处的分位数
which.max(x)返回向量x中最大值位置(索引值）
which(x==7)
which(x>5)
'''


'''
矩阵
colsums(x)计算矩阵中每列的和
rowcums(x)计算矩阵中没行的和
colmeans(x)
rowmeans(x)计算矩阵中没行的平均值
diag(x)返回矩阵x的对角线
t(x)转置矩阵
'''


'''
列表和向量在模式上类似，都是数据的集合，但是向量只能存储一种数据类型，列表中的对象可以是
R中的任何数据模式，甚至是列表本身
列表$(行或者列)可以直接访问列表中的行或者列
mlist[5] <- iris 在列表中添加新的列表
mlist[5] <- NULL 删除赋值得的列表
mlist[-5] <- mlist
'''

'''
数据框
数据集通常是由数据构成的一个矩阵数组，行表示观测，列表示变量。
将每一列保存为向量，最后x <- data.frame(向量)及可将所有的向量连接在一起保存为数据框
attach(数据框名称)加载数据框到目录中，加载完成后可以直接输入不带引号的列名称，直接引用列
使用完数据后，使用detach（x）取消加载
'''

'''
因子（是一个向量）
变量的额分类：名义型变量（质量性状），有序型变量，连续型变量（数量性状）。
在R中名义型变量和有序型变量称为因子，factor。这些分类变量的可能值称为一个水平，level，如good,better,都称为一个level
这些水平构成的向量就称为因子
table(x)对数据框中某一列作为因子类型进行分类频数统计
f <- factor(c('x','y'))用来定义因子（将向量转化因子）
f <- factor(c('x','y'), ordered = T, levels = c('x', 'y'))通过这样设定不同水平顺序
返回levels：x<y
绘图时，向量绘制的是散点图，因子绘制的是条形图
cut（x，c（seq（0,100,10）））将向量中连续值按照每10个进行切分成每个因子，有利于之后的频次统计
state.division和state.region是因子类型的数据
'''


'''
在R中使用NA代表缺失值，not avaliable的简称，用来存储缺失信息
但NA不是确定的值，他可以是任何值，NA与零是完全不同的
1+NA=NA
一旦数据集中有NA将无法计算
在计算函数中添加na.rm=T可以将NA值删除
但是直接计算时添加na.rm=T无法知道数据集之前是否含有NA值
is.na(x)如或返回中有TRUE则数据集中对应位置为NA
使用y <- na.omit(x)函数生成一个没有NA值的数据集
但是当使用na.omit处理一个数据框时则是删除数据框中的一行(即一个观测)
'''

'''
字符串
nchar("HEllo World")中nchar可以统计括号中字符串的长度，空格也算一个字符的长度
length（x）返回的是数据集中元素的个数
paste可以将多个向量合并成一个向量
paste（x,x,x,sep = '-')设置-为连字符
将一个向量与一个元素向连接，结果输出向量中的每个元素分别与那个单独元素连接（paste）
substr（x=,start = 1,stop = 3 ）提取x向量中每个字符串中前三个字符
toupper（x）可以将x向量中的字符串进行大写处理
tolower(x)
grep(’A+‘，x,fixed = T)在x数据集中匹配是否有A+ ，fixed表示为是否使用正则表达式
strsplit（字符串，分隔符）返回一个列表
生成两个向量的所有组合（笛卡尔积）使用outer（x,y,FUN =paste,sep = ''）
'''

'''
时间序列分析
as.Data(x,format = '%Y-%m-%d'),将x向量转化为固定格式的日期
seq(as.Data('2017-01-01'),as.Data('2017-07-05'),by = 5) 生成一个时间序列
round()取向量中的整数
runif()生成随机数
ts（x,start = ,end = ,frequency = 1/4/12）生成时间序列， freq = 1为一年为频率，4为一个季度，12为每个月

 
'''


'''
常见错误
数据类型
c(),如果定义的是一个集合必须加c
matrix()
array()
data.frame()
定义符号<-(ALt+-可以自动生成)
安装包时添加’‘
数据框索引的时候[]中取行或者列记得加,

'''