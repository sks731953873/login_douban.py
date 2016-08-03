
import urllib.request
import re
import os
import random
img_addrs = []
post_url = []

def url_open(page_url):#打开网址获取源码模块
    req = urllib.request.Request(page_url) #简化函数
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36') #增加header信息
    response =urllib.request.urlopen(page_url) #打开所需网址
    html = response.read() #读取网页信息
    return html
    
def find_posturl(page_url): #找寻帖子地址模块
    print('帖子列表地址',page_url)
    html = url_open(page_url).decode('UTF-8') #解码网页信息

    a = html.find('<!--- douban ad end -->') #找寻网页源代码中，独特的标记信息
    b = html.find('td class=',a)            #截取帖子链接前表头1
    while b != -1:
        c = html.find('a href=',b)          #截取帖子链接前表头2
        d = html.find('title=',c)           #截取帖子链接后表头
        d = d + 7
        b = html.find('td class',d)         #判断是否还有帖子链接
        post_url.append(html[c+8:d-9])      #截获帖子链接并加入帖子链接列表
        
    return post_url

def find_imgs(img_url): #找寻图片地址模块
    html = url_open(img_url).decode('UTF-8') #解码网页信息
    a = html.find('topic-content clearfix') #找寻网页源代码中，独特的标记信息
    d = html.find('fav-add btn-fav') #豆瓣贴中，标记为喜欢的代码，位于帖子正文的末尾
    if a != -1:
        b = html.find('img src=',a)  #截取图片链接前表头
        if b != -1:
            c = html.find('jpg',b)   #截取图片链接后表头
            while c !=-1:
                img_addrs.append(html[b + 9:c + 3]) #截获图片链接并加入图片链接列表
                print('图片地址:',html[b + 9:c + 3])
                b = c + 4
                b = html.find('img src=',b,d)  #判断是否还有新的图片（一帖多图）
                c = html.find('jpg',b)
                if b == -1:
                    c = -1
    return img_addrs

def save_imgs(folder,img_addrs): #保存图片模块
    imgaddrs_num = 0
    for each in img_addrs:       #用循环分割图片链接列表
        con = img_addrs[imgaddrs_num]
        print('图片地址=',con)
        filename = con.split('/')[-1]
        print('图片名=',filename)#以获取的单个图片链接的末尾字符串为文件名
        imgaddrs = img_addrs[imgaddrs_num] #分割图片链接列表
        with open(filename,'wb') as f:  #写入文件名
                img = url_open(imgaddrs)#写入文件信息
                f.write(img)            #写入图片信息
        imgaddrs_num = imgaddrs_num + 1
        print('图片数量=',imgaddrs_num)
       
def download_db(folder='douban',pages = 5): #想要down几页，帖子列表从0页开始 0页即第一页
    os.mkdir(folder)
    os.chdir(folder)
    url = 'https://www.douban.com/group/haixiuzu/discussion?start='
    n = 0   #起始多少页开始
    page = 0
    while page <= pages:
        page_num = n * 25 #豆瓣小组25个帖子为1页
        page_url = url + str(page_num)
        posturl_addrs = find_posturl(page_url)      
        m=0
        print('页数=',n)
        n = n + 1
        page = page + 1
    num = len(posturl_addrs)
    m = 0
    for i in range(num):              #分割帖子地址列表
        img_url = posturl_addrs[m]  #获取单独帖子地址
        print('帖子地址:',img_url)
        img_addrs = find_imgs(img_url)
        m = m + 1
    save_imgs(folder,img_addrs)
    
        
if __name__ =='__main__':
    download_db()
