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
