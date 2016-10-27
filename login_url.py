# -- coding:gbk --
import re
import urllib, urllib2, cookielib
 
loginurl = 'https://www.douban.com/accounts/login'
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
 
params = {
"form_email":"your email",
"form_password":"your password",
"source":"index_nav" #没有的话登录不成功
}
 
#从首页提交登录
response=opener.open(loginurl, urllib.urlencode(params))
 
#验证成功跳转至登录页
if response.geturl() == "https://www.douban.com/accounts/login":
    html=response.read()
 
    #验证码图片地址
    imgurl=re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url=imgurl.group(1)
        #将图片保存至同目录下
        res=urllib.urlretrieve(url, 'v.jpg')
        #获取captcha-id参数
        captcha=re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>' ,html)
        if captcha:
            vcode=raw_input('请输入图片上的验证码：')
            params["captcha-solution"] = vcode
            params["captcha-id"] = captcha.group(1)
            params["user_login"] = "登录"
            #提交验证码验证
            response=opener.open(loginurl, urllib.urlencode(params))
            ''' 登录成功跳转至首页 '''
            if response.geturl() == "http://www.douban.com/":
                print 'login success ! '
