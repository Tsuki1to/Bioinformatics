from Bio.Seq import Seq,back_transcribe

def work():
    while True:
        my_seq = Seq(input('\n请输入DNA、RNA或protein序列(Ctrl+Z后按Enter退出进程)：'))
        print('\
        1、互补链序列\n\
        2、反向互补链序列\n\
        3、首尾颠倒\n\
        4、DNA转录成RNA\n\
        5、RNA反转录成cDNA\n\
        6、DNA/RNA序列翻译成蛋白质\n\
        7、转为小写\n\
        8、转为大写\n\
        9、退出系统')
        function = input('请选择功能,输入相应序号: ')
        if function == '1':
            print('\n互补链序列: 3\' -', my_seq.complement(), '- 5\'\n长度：', len(my_seq.complement()), 'bp')
        elif function == '2':
            print('\n反向互补链序列: 5\' -', my_seq.reverse_complement(), '- 3\'\n长度：', len(my_seq.reverse_complement()), 'bp')
        elif function == '3':
            print('\n首尾颠倒: ', my_seq[::-1], '\n长度：', len(my_seq[::-1]), 'bp')
        elif function == '4':
            print('\nDNA转录成RNA: 5\' -', my_seq.reverse_complement().transcribe(),'- 3\'\n、长度：',len(my_seq.reverse_complement().transcribe()), 'bp')
        elif function == '5':
            my_seq_str = str(my_seq)
            if'T' in my_seq_str:
                print('请输入RNA序列：')
            elif't' in my_seq_str:
                print('请输入RNA序列：')
            else:
                print('\nRNA反转录成cDNA: 5\' -', back_transcribe(my_seq_str), '- 3\'\n长度：', len(back_transcribe(my_seq_str)), 'bp')
        elif function == '6':
            print('\nDNA/RNA序列翻译成蛋白质: ', my_seq.translate(), '\n氨基酸数量：', len(my_seq.translate()))
        elif function == '7':
            print('\n小写序列：', my_seq.lower(), '\n长度：', len(my_seq.lower()), 'bp')
        elif function == '8':
            print('\n大写序列：', my_seq.upper(), '\n长度：', len(my_seq.upper()), 'bp')
        elif function =='9':
            break
        else:
            print('\n请检查序列是否正确')



if __name__ == '__main__':
    work()
