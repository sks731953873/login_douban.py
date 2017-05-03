# -*- coding:utf-8 -*-
from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
import re
import os




def getHtmls(url):  # 返回每个显示图片的链接列表
    bsObj = url_open(url)
    hrefs = bsObj.findAll('a', href=re.compile('^\/photos\/.+(.html)$'))
    htmls = []
    for href in hrefs:
        wholeHtml = 'http://www.xiumm.cc' + href.attrs['href']  # 拼接成完整链接
        if wholeHtml not in htmls:
            htmls.append(wholeHtml)
    return htmls


def setImgurls(url, images):
    bsObj = url_open(url)
    imageUrls = bsObj.findAll('img', src=re.compile('\/data\/.+(.jpg)$'))  # 匹配所有包含/data/的链接
    for imageUrl in imageUrls:
        wholeImage = 'http://www.xiumm.cc' + imageUrl.attrs['src']
        alt = imageUrl.attrs['alt']
        imgUrl_alt = wholeImage + '====' + alt
        # print(wholeImage)
        images.append(imgUrl_alt)


def getImages(urls, ii, savePath):  # 返回图片的链接列表
    for url in urls:
        number = getFenLastPageNum(url)  # 爬取此url页面的所有同级页面的页数number
        print(number)
        images = []
        for i in range(1, number + 1):  # 从1到number(不包含后面这项的本身)
            if i == 1:
                setImgurls(url, images)
                print(url)
            else:
                if i == 2:
                    url = url.split('.html')[0] + '-' + str(i) + '.' + url.split('.')[-1]  # 将例如-10拼凑到.html的前面
                    print(url)
                    setImgurls(url, images)
                elif i > 2:
                    url = url.split('-' + str(i - 1) + '.html')[0] + '-' + str(i) + '.' + url.split('.')[
                        -1]  # 将例如-10拼凑到.html的前面
                    print(url)
                    setImgurls(url, images)
        for imageUrl_alt in images:
            filterImgUrl = 'http://www.xiumm.cc' + imageUrl_alt.split('====')[0].split('http://www.xiumm.cc')[
                -1]  # 过滤掉多出来的地址内容
            alt = imageUrl_alt.split('====')[1].split('_')[0]
            print('image url:' + filterImgUrl)
            path(ii, savePath, alt)
            saveImg(filterImgUrl)


def saveImg(url):  # 根据一个图片链接保存图片文件
    filename = url.split('/')[-1]
    if not os.path.exists(filename):  # 如果此文件不存在
        urlretrieve(url, filename)


def getHomeLastPageNum(url):  # 返回最后一页的数字
    bsObj = url_open(url)
    albumPages = bsObj.findAll('a', href=re.compile('^\/albums\/page-.+.html$'))  # 匹配出所有跟主页同级的链接集合
    num = albumPages[-2].get_text()  # 倒数第二页显示的是最后一页图片网页链接
    return int(num)


def getFenLastPageNum(url):  # 返回最后一页的数字
    bsObj = url_open(url)
    photoPages = bsObj.findAll('a', href=re.compile('^\/photos\/.+.html$'))  # 匹配出所有跟主页的子页同级的链接集合
    num = photoPages[-2].get_text()  # 倒数第二页显示的是最后一页图片网页链接
    return int(num)


def url_open(url):
    html = urlopen(url).read()
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj


def path(i, savePath, alt):
    if not os.path.exists(savePath + 'Girls\\img' + str(i) + '\\' + alt):  # 如果不存在此文件夹
        os.makedirs(savePath + 'Girls\\img' + str(i) + '\\' + alt)
        os.chdir(savePath + 'Girls\\img' + str(i) + '\\' + alt)
    else:
        os.chdir(savePath + 'Girls\\img' + str(i) + '\\' + alt)


def main():
    url = 'http://www.xiumm.org/'
    lastPageNum = getHomeLastPageNum(url)
    savePath = input('请输入要下载的路径(格式是D:\\):')
    for i in range(1, lastPageNum + 1):
        if i == 1:
            htmls = getHtmls(url)
            getImages(htmls, i, savePath)
        else:
            path(i, savePath)
            url = url + 'albums/page-' + str(i) + '.html'
            htmls = getHtmls(url)
            getImages(htmls, i, savePath)


if __name__ == '__main__':
    main()
