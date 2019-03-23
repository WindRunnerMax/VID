#!/usr/bin/python 
# -*- coding: utf-8 -*-
# pyuic5 form.ui -o form.py

import time
import requests
import re
import os
import sys
import json
import datetime
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui
from form import Ui_Form

VUrl = "http://v.douyin.com/YmuKu5/"

VHEADERS = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.65',
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"accept-encoding":"gzip, deflate, sdch, br",
"accept-language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
"cache-control":"no-cache"
}
VH1 = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.65"
VH2 = "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3"

class Vibrato(QDialog,Ui_Form):
    """docstring for Vibrato"""
    def __init__(self,parent=None):
        super(Vibrato, self).__init__(parent)
        self.setupUi(self)
        self.url = VUrl
        self.HEADERS = VHEADERS

    def GetRealUrl(self):
        session = requests.Session()
        req = session.get(self.url , timeout = 5 , headers = self.HEADERS)
        req.encoding = 'utf-8'
        data = req.text
        cover = data.split("cover: \"")[1].split("\"")[0]
        playAddr = data.split("playAddr: \"")[1].split("\",")[0]
        videoId = playAddr.split("video_id=")[1].split("&")[0]
        videoAddr = playAddr.replace("/playwm/","/play/");
        return {
            "cover": cover,
            "playAddr": playAddr,
            "addr": videoAddr,
            "id": videoId
        },session

    def Download(self,info,session):
        VHEADERS['User-Agent'] = VH2
        videoBin = session.get( info['addr'],timeout=5, headers = VHEADERS );
        filename = info['id'];
        with open('%s.mp4' % (filename),'wb') as fb: # 将下载的图片保存到对应的文件夹中
            fb.write(videoBin.content)
            self.label.setText("下载完成")
        VHEADERS['User-Agent'] = VH1

    def run(self):
        self.label.setText("稍等")
        QApplication.processEvents()
        try:
            self.url = self.lineEdit.text()
            if self.url == "":
                self.label.setText("链接不能为空")
            else :
                regx=r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+" 
                pattern=re.compile(regx) 
                listurl=re.findall(pattern,repr(self.url))
                if len(listurl) == 0:
                    self.label.setText("解析链接失败")
                else:
                    if listurl[0][len(listurl[0])-1] == "'":
                        listurl[0] = listurl[0][:-1]
                    self.url = listurl[0]
                    info,session = self.GetRealUrl()
                    self.Download(info,session)
        except Exception as e:
                self.label.setText(str(e))
        
    def test(self):
        try:
            info,session = self.GetRealUrl()
            self.Download(info,session)
        except Exception as e:
            print("内部错误")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dlg=Vibrato()
    dlg.show()
    sys.exit(app.exec_())

# if __name__ == '__main__':
#     VI=Vibrato()
#     VI.test()

