# -*- encoding=utf8 -*-
__author__ = "dglr"

from airtest.core.api import *

auto_setup(__file__)

from airtest.core.api import *
from base64 import b64decode
import cv2
import numpy as np
import sys


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

animal = ["background/bee.jpg", "background/butterfly.jpg", "background/carrot.jpg", "background/cat.jpg", "background/monkey.jpg", "background/squirrel.jpg"]


def isEqual(img1, img2):
    result = cv2.addWeighted(img1, 1, img2, -1, 0)
    result2 = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
    return result2

def getResult(img):
    _max = sys.maxsize
    answer = np.empty_like(img)
    for name in animal:
        img_bg = cv2.imread(name)
        result = isEqual(img, img_bg)
        new_result = normalize(result)
        max = new_result.sum()
        if max < _max:
            answer = new_result
            _max = max
    return answer

def normalize(img):
    shape = img.shape
    new_img = np.zeros_like(img)
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            if img[i, j] > 10:
                new_img[i, j] = 255
    return new_img

def find_lens(img):
    start = False
    zero = False
    line = img.max(axis=0)
    lens = 0
    s_lens = 0
    for i in range(0, len(line)):
        if not start:
            if line[i] > 0 and i < len(line) - 1 and line[i + 1] > 0:
                start = True
            else:
                s_lens += 1

        elif start and not zero:
            if line[i] == 0 and i < len(line) - 1 and line[i + 1] == 0:
                zero = True
            lens += 1
        elif start and zero:
            if line[i] > 0 and i < len(line) - 1 and line[i + 1] > 0:
                return s_lens, lens
            lens += 1

    assert("here is an error, can not find 2 blocks")
    return s_lens, -1

def get_lens(name):
    img = cv2.imread(name)
    result = getResult(img)
    cv2.imshow("answer!", result)
    cv2.waitKey()
    s_lens, lens = find_lens(result)
    return s_lens, lens


texts = ["14:00-", "14:30-", "15:00-","15:30-","16:00-","16:30-","17:00-","17:30-","18:00-","18:30-","19:00-","19:30-","20:00-"]


from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# success = poco("安安车生活").exists()
# if not success:
#     log("can not open app")
# poco("安安车生活").click()
# success = poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.safeluck.life:id/navigation").offspring("首页").child("com.safeluck.life:id/icon").exists()

# if not success:
#     print("open app failed!")
#     #未能打开界面
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.safeluck.life:id/navigation").offspring("首页").child("com.safeluck.life:id/icon").click()

poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.safeluck.life:id/navigation").offspring("教学管理").child("com.safeluck.life:id/icon").click()
poco(text="预约培训").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.safeluck.life:id/webview").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[3].child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.safeluck.life:id/webview").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[1].child("android.view.View")[0].child("android.view.View").offspring("android.widget.ListView").child("android.view.View")[1].click()

poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.safeluck.life:id/webview").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[1].child("android.view.View")[2].child("android.widget.TextView")[1].click()



poco.swipe([0.5,0.9],[0.5,0.3])

texts = ["14:00-", "14:30-", "15:00-","15:30-","16:00-","16:30-","17:00-","17:30-","18:00-","18:30-","19:00-","19:30-","20:00-"]

empty = False

for i in poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.safeluck.life:id/webview").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[2].child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View"):
  if len(i.child("android.view.View"))< 5:
   continue
  if i.child("android.view.View")[1].get_text() not in texts:
  click_node = i.child("android.view.View")[4]
  text = click_node.get_text()
  if text == "已约满":
   log(i.child("android.view.View")[1].get_text() + "时间段已满")
  elif text == "预约":
   click_node.click()
   empty = True
   break
if not empty:
 log("菜鸡，没有空余位置")

    
   



    poco(text=" 已预约").click()



empty = False
for text in texts:
  node_2 = poco(text=text)
  print(node_2.get_text()) 
  node_p = node_2.parent()
  print(node_p)
  node = node_p.child("android.view.View")[6]
  result = node.get_text
  print(result)
  if result == "已约满":
   log.logger.Info(text + "时间段已满")
  else:
   node.click()
   empty = True
   break
if not empty:
 log.logger.Info("菜鸡，没有空余位置")


        






# poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.safeluck.life:id/webview").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[2].child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.view.View")[6].click()








# poco(text="预约").click()

# 抵达安全验证区域


b64img, fmt = poco.snapshot(width=720)
open(str(id) + 'screen.{}'.format(fmt), 'wb').write(b64decode(b64img))
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
    "com.safeluck.life:id/webview").child("android.webkit.WebView").child("android.webkit.WebView").child(
    "android.view.View").child("android.view.View")[1].child("android.view.View")[11].child(
    "android.view.View").child("android.view.View")[0].child("android.view.View").click()
poco(text="确认预约").click()
id += 1

# 完成截图，保存在screen.png里面

img = cv2.imread("screen.jpg")

img1_background = img[566:748, 39:684]

cv2.imwrite("real_background.jpg", img1_background)

name = "real_background.jpg"



