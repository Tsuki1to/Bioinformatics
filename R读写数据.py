# 开发时间：2023/1/5/0005 上午 11:26

'''
R添加数据
1.通过键盘录入数据
通过设置不同向量集然后data.frame数据框统计
data <- edit(data)
fix(data)
2.通过读取存储文件的方式获取数据
3.通过访问数据库获取数据
ODBC
Open Database Connectivity
RODBC包
help(package = 'foreign') foreign包可以读取多种格式的文件
x <- read.table('clipboard', header = T, sep = '/t')
readclipboard()

R读取压缩文件的内容：read.table(gzfile('xxx.txt.gz'))
当读取的文件不够规整时，无法使用read.table整体提取，只能使用readLines()分开读取每行的内容
readLines('xxxxx',n = 15)其中n = 可以限制最大读行数

scan函数可以读取数据的单元
'''


'''
help(package = 'foreign')可以查看可以读写的文件格式
cat(x)直接将内容显示在屏幕上
write(x,file = 'x.txt')x可以是一个向量可以是一个矩阵、数据框
write.table(iris,file = 'newfile.csv',append = TRUE)在源文件中添加新的数据框
write.table(mtcars,gzfile('newfile.csv.gz'),sep = ',')将数据框直接写入包含CSV的压缩包


'''