#coding:utf-8

import urllib
import urllib2
import cookielib
import gzip
from StringIO import StringIO
import re
import urlparse

#def getCompressedPage():

proxy = {'http':'http://10.191.131.3:3128'}
	
urllib2.ProxyHandler(proxy)
cookiejar = cookielib.LWPCookieJar()

fileName = 'cookie.txt'

#声明一个MozillaCookie对象实力来保存cookie，之后写入文件

cookie = cookielib.MozillaCookieJar(fileName)
try:
	cookiejar.load('cookie.txt', ignore_discard=True, ignore_expires=True)
except IOError:
	print('Cookie not loaded')

cookieSupport = urllib2.HTTPCookieProcessor(cookiejar)

opener = urllib2.build_opener(cookieSupport, urllib2.HTTPHandler)
#urllib2.install_opener(opener)

Cookie = "s_vnum_n2_us=4%7C1%2C35%7C1%2C1%7C1%2C3%7C1; dssid2=3e197512-a89e-415d-ad89-6fd436d66200; dssf=1; optimizelyEndUserId=oeu1471254232102r0.004721867290524484; pxro=1; optimizelySegments=%7B%22341793217%22%3A%22direct%22%2C%22341794206%22%3A%22false%22%2C%22341824156%22%3A%22gc%22%2C%22341932127%22%3A%22none%22%7D; s_vi=[CS]v1|2BBF12B185011953-40000109800042EA[CE]; optimizelyBuckets=%7B%7D; s_fid=17E19E15C01BB5B8-0D9DC48130E81357; clientTimeOffsetCookie=28800000; site=USA"
ClientInfo="%7B%22U%22%3A%22Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_11_3%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F52.0.2743.116+Safari%2F537.36%22%2C%22L%22%3A%22en-US%22%2C%22Z%22%3A%22GMT%2B08%3A00%22%2C%22V%22%3A%221.1%22%2C%22F%22%3A%22NGa44j1e3NlY5BSo9z4ofjb75PaK4Vpjt3Q9cUVlOrXTAxw63UYOKES5jfzmkflHfmNzl998tp7ppfAaZ6m1CdC5MQjGejuTDRNziCvTDfWl_LwpHWIO_0vLG9mhORoVidPZW2AUMnGWVQdgMVQdgGgeVjrkRGjftckcKyAd65hz7YOK2w5ADwIlUjVsYwQ9dvcpxUyL4T9KTI6y8GGEDd5ihORoVyFGh8cmvSuCKzIlnY6xljQlpRDBeraeJ9QBcEPm8LKfAaZ4ySy.aPjftckvIhIDLTK43xbJlpMpwoNSUC56MnGWpwoNHHACVZXnN95Mfp2qB3dKBSQVD_DJhCizgzH_y3EjNpmd.1wcDhveKQ6TtLB.Tf5.EKVdIX_DJF0ixAzcUeAvqCSFQ_H.4tFaiK7.MJZNqhyA_r_LwwKdBvpZfWfUXtStKjE4PIDzp9hyr1BNlrAp5BNlan0Os5Apw..w1%22%7D"
	
i_header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:45.0) Gecko/20100101 Firefox/45.0",
		"Accept-Encoding":"gzip, deflate, br",
		"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		"Upgrade-Insecure-Requests":"1",
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Referer":"https://idmsa.apple.com/IDMSWebAuth/signin?appIdKey=77e2a60d4bdfa6b7311c854a56505800be3c24e3a27a670098ff61b69fc5214b&sslEnabled=true&rv=3",
		"Host":"idmsa.apple.com",
		"Connection":"keep-alive",}

data = {}
data['appleId'] = 'bill_chen2'
data['pwd'] = 'Panic_007'
data['remember-me'] = 'false'
post_data = urllib.urlencode(data).encode('utf-8')
print(post_data)

url = 'https://bugreport.apple.com/'
url1= 'https://idmsa.apple.com/IDMSWebAuth/authenticate'
url2= 'https://idmsa.apple.com/IDMSWebAuth/signin'
cookie_support = urllib2.HTTPCookieProcessor(cookiejar)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
opener.addheaders = [(key, value) for key, value in i_header.items()]


cookie.save(ignore_discard=True, ignore_expires=True)

def decompressedPage():

	r = opener.open(url)

	if r.info().get('Content-Encoding') == 'gzip':
		buf = StringIO(r.read())
		f = gzip.GzipFile(fileobj=buf)

		html = f.read().decode('utf-8')
		print(html)		
		appIdKey = re.findall(r'<input type="hidden" id="appIdKey" name="appIdKey"\n\s*?value="(.*?)" />', html)[0]
		print(appIdKey)			
		
		data['appIdKey'] = appIdKey

		post_data = urllib.urlencode(data).encode('utf-8')
		print(post_data) 
		r = opener.open(url1, post_data)
		print('r.geturl(): %s' % r.geturl())
#       cookiejar.save(ignore_discard=True, ignore_expires=True)
		print('r.read(): %s' % r.read())

		if r.info().get('Content-Encoding') == 'gzip':
			buf = StringIO(r.read)
			print(buf)
			f = gzip.GzipFile(fileobj=buf)
			print(f)
			html = f.read().decode('utf-8')
			print('html: %s' % html)
		cookiejar.save(ignore_discard=True, ignore_expires=True)			


if __name__ == "__main__":

#	response = getCompressedPage()
	decompressedPage()

	
	







