# _*_ coding: utf-8 _*_
# 用 argv 来获取文件名
# from sys import argv
# argv 是本文件名 和要读取的文件名
# script, filename = argv
# 用函数 open 打开文件
# 打印出这个文件名
print "Here's your filename:"
filename = raw_input (">")
txt = open(filename)
# 读取出文件里的内容
print txt.readline()


# 以上子啊执行一次
print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.readlines()


print "Here's your filename2:"
filename2 = raw_input (">")
txt = open(filename)
# 读取出文件里的内容
print txt.read()
txt.close()

