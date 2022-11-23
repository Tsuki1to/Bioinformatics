# 开发时间：2022/11/23 16:17
import Bio
from Bio.Seq import Seq
my_seq = Seq('AGTACACTGGTA')
print('序列反向互补后为：',my_seq.reverse_complement())
print('序列互补后为：',my_seq.complement())
print('序列转录后为：',my_seq.transcribe())
print('序列翻译为蛋白后为：',my_seq.translate())