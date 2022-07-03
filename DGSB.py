# -*- encoding=utf8 -*-
__author__ = "ziyuc"
from python_try import get_lens
from airtest.core.api import *
from base64 import b64decode
import cv2
import numpy as np

auto_setup(__file__)

id = 1
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 抵达安全验证区域

for i in range(0, 50):
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
start_lens, lens = get_lens(name)
