#coding=utf-8
import pymouse
import time
import Quartz
import LaunchServices
from Cocoa import NSURL
import Quartz.CoreGraphics as CG
from PIL import Image
import pytesseract
import webbrowser

class Positions():

    def __init__(self):
        self.mouse = pymouse.PyMouse()

    def get_point(self):
        try:
            print('正在采集坐标1，请将鼠标移动到左上角')
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            (x1,y1) = self.mouse.position()
            print('成功!坐标：(%f, %f)' %(x1, y1))
            print('')
            print('正在采集坐标2，请将鼠标移动到右下角')
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            (x2,y2) = self.mouse.position()
            print('成功!坐标：(%f, %f)' %(x2, y2))
            return (x1, y1, x2, y2)
        except KeyboardInterrupt:
            print('获取失败')

    def screenshot(self,path,region = None):
        if region is None:
            region = CG.CGRectInfinite
        image = CG.CGWindowListCreateImage(
            region,
            CG.kCGWindowListOptionOnScreenOnly,
            CG.kCGNullWindowID,
            CG.kCGWindowImageDefault
        )
        dpi = 72
        url = NSURL.fileURLWithPath_(path)
        dest = Quartz.CGImageDestinationCreateWithURL(
        url,
        LaunchServices.kUTTypePNG,
        1,
        None
        )
        properties = {
        Quartz.kCGImagePropertyDPIWidth: dpi,
        Quartz.kCGImagePropertyDPIHeight: dpi,
        }
        Quartz.CGImageDestinationAddImage(dest, image, properties)
        Quartz.CGImageDestinationFinalize(dest)

    def trans_pic(self,path):
        pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/3.05.01/bin/tesseract'
        tessdata_dir_config = '--tessdata-dir "/usr/local/Cellar/tesseract/3.05.01/share/tessdata"'
        text = pytesseract.image_to_string(Image.open(path),lang='chi_sim',config=tessdata_dir_config)
        text = ''.join(text.split())
        return text

'''
a = Positions()
(x1,y1,x2,y2) = a.get_point()
region = CG.CGRectMake(x1,y1,x2,y2)
file_path = "/Users/didi/Safe/Study/MyFun/screeshot.png"
a.screenshot(file_path,region=region)
text = a.trans_pic(file_path)
print text
#url = 'http://www.baidu.com/s?wd='+text
url = 'https://www.baidu.com/baidu?wd='+text+'&tn=cnopera&ie=utf-8'
print url
webbrowser.open(url)
'''

