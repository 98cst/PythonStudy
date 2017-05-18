#encoding:utf-8
import re
import requests
import time
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")  #设置默认的string的编码格式

#爬取第一个网站
#转换月份
def month_trans(string):
    list1 = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    list2 = ['01','02','03','04','05','06','07','08','09','10','11','12']
    return list2[list1.index(string)]

# 把时间转为标准时间格式
def standtime_trans():
    return standard_time

if __name__ == '__main__':


#该网站的新闻共有56页，每页4篇新闻
    j = 1        #j为计数器，记录爬取的新闻数
    for i in range(1,57):        #i为页码数
        flag = 0        #辅助爬取新闻分类的类别
        url = "https://www.gov.sg/news/page-" + str(i)
        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
        headers = {'User_Agent' : user_agent}
        response = requests.get(url= url,headers = headers)
        response.encoding = "utf-8"
        html = response.text

        list = re.findall(r'<a href=".*" class="article-read rs_skip"', html)   # list:4news_url
            #print list
        classification = re.findall(r'<span class="category">(.*?)</span>\r',html)
        #得到每一个新闻的对应类别

        for line in list:
            try:
                url = "https://www.gov.sg" + re.search(r'<a href="(.*?)" class=', line).group(1)
                #获取URL，以便得到源代码
                    #print url
                news_html = requests.get(url,headers = headers).text.decode('utf-8')
                with open('./gov.sg/html/'+str(j)+'.html','w')as f1:
                    f1.write(news_html)                #把源代码写进.html的文件中
                    f1.flush()
                    f1.close()

                    # 把时间转为标准时间格式
                url_time = re.search(r'<span class="date">(.*?)By', news_html).group(1)
                new_time = url_time.replace('&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;','')
                new_time = re.split(' ', new_time)
                standard_time = new_time[2] + '-' + month_trans(new_time[1]) + '-' + new_time[0] + ' 00:00:00'
                    #print standard_time

                    # 把字符串时间转换为时间戳:
                timeArray = time.strptime(standard_time, "%Y-%m-%d %H:%M:%S")
                timeStamp = int(time.mktime(timeArray))

                    #把正文中的<br />去掉>
                    #print type(html2.encode("utf-8"))
                news_body = re.findall('src="[\w\W]*?\.jpg"[\w\W]*?><br>([\w\W]*?)Source:',news_html)
                body = news_body[0].replace("<br />\n<br />","")
                    #print body

                    #外链接的正则匹配
                out_link = re.findall(r'<h2><a href="(.*?)">',news_html)
                for line in out_link:
                    url_out_links = "https://www.gov.sg" +line

                    #标题的正则匹配
                title = re.findall(r'<h2 class="title">([\w\W]*?)</h2>', news_html)
                for line in title:
                    title = line.strip('\r\n            ')
                        #print title

                    #创建字典
                dict = {
                    'news_id': j,
                    'source_id': "62",
                    'language': "sin",
                    'request_url': url,
                    'response_url': response.url,
                    'classification': classification[flag],
                    'title': title,
                    'abstract': re.findall(r'<p><p>(.*?)</p></p>',news_html) ,
                    'body': body,
                    'pub_time':  standard_time,
                    'cole_time': timeStamp,
                    'out_links': url_out_links,
                    'images' : re.findall(r'<br><img src="(.*?)" alt=',news_html)
                }
                flag = +1
                    # print dict

                with open('./gov.sg/json/'+str(j)+'.json','w')as f2:
                    f2.write(json.dumps(dict))
                    f2.flush()
                    f2.close()
                j += 1
                i += 1
            except:
                with open('./gov.sg/extra_html/'+str(j)+'.html','w')as f3:
                    f3.write(news_html)                #把不能爬取的源代码写进.html的文件中
                    f3.flush()
                    f3.close()
            finally:
                print "ok"

