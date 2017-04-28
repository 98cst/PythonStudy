该代码是用字符串匹配的方法来实现的。首先新建一个字典，读取评论点的文件把关键词录入成为字典的键，录入时要去掉空格，先初始化每个键的值为0，再读取评论文件的每一行，进行字符串匹配，用一个计数器来实现统计，最后把结果录入一个新建的文本文件中，其中包含关键词及各个统计量。
对于评论文件的访问路径，由
file = open('/home/cu/Desktop/太空旅客.txt','r')
goalfile = file.readlines()
实现。
而各个评论点的文件访问路径，导入一个OS的包，由
for p,dirs,files in os.walk('/home/cu/Desktop/词典'):
    for f in files:
        # print os.path.join(p,f)
        with open(os.path.join(p,f)) as f:
实现。
