##当用户输入文件名和需要打印的行数（N）时，将文件前N行打印

def file_view(file_name, line_num):
    print('\n文件%s的前%s的内容如下：\n' % (file_name, line_num))
    f = open(file_name)
    for i in range(int(line_num)):
        print(f.readline(), end= '')

    f.close()

file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
line_num = input('请输入需要显示该文件前几行：')
file_view(file_name, line_num)
