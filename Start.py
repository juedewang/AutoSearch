# -*- coding: cp936 -*-
# -*- coding: encoding -*-
from GetMouse import Positions
import Quartz.CoreGraphics as CG
import webbrowser
import os
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import urllib

a = Positions()
(x1,y1,x2,y2) = (148.765625, 125.15234375, 853.51171875, 1175.09375)
region = CG.CGRectMake(x1,y1,x2,y2)
file_path = "./MyFun/screeshot.png"
a.screenshot(file_path,region=region)
text = a.trans_pic(file_path)
print(text.__class__)
print(text)
#url = "https://www.baidu.com/s?wd=%s&tn=cnopera&ie=utf-8" %text
text_uni = text.encode('utf-8')
text_url = urllib.quote(text_uni)
url = u"https://www.baidu.com/s?wd=%s" %text_url
print(url)
os.system("python -m webbrowser -t "+url)
webbrowser.open(url)
