#encoding:utf-8
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#连接数据库
conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '980512win',
    charset = "utf8",
    db = 'university',
)

# 获取数据库执行游标
cur = conn.cursor()
#分别打开三个数据文本，把数据传到数据库中的三个表格
f1 = open("/home/cu/homework/homework4/department.txt",'r')
dept = f1.readlines()
for line in dept:
    line = line.strip('\n')
    line = line.split(' ')
    cur.execute("insert into department values(%s,%s,%s)",(line[0], line[1], line[2]))
    conn.commit()

f2 = open("/home/cu/homework/homework4/student.txt", 'r')
student = f2.readlines()
for line in student:
    line = line.strip('\n')
    line = line.split(' ')
    cur.execute("insert into student values(%s,%s,%s,%s,%s,%s)",(line[0],line[1],line[2],line[3],line[4],line[5]))
    conn.commit()

f3 = open("/home/cu/homework/homework4/exam.txt",'r')
exam = f3.readlines()
for line in exam:
    line = line.strip('\n')
    line = line.split(' ')
    cur.execute("insert into exam values(%s,%s,%s)",[line[0], line[1], line[2]])
    conn.commit()

cur.close()
conn.close()

