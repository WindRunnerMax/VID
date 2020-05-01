#!/usr/bin/python 
# -*- coding: utf-8 -*-

import re
import requests

HEADERS = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-encoding":"gzip, deflate, sdch, br",
    "accept-language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
    "cache-control":"no-cache",
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
}

H0 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
H1 = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"


class Vibrato():
    """docstring for Vibrato"""
    def __init__(self):
        super(Vibrato, self).__init__()
        self.url = "https://v.douyin.com/nMuYtN/"
        self.headers = HEADERS

    def __get_real_url(self):
        session = requests.Session()
        req = session.get(self.url , timeout = 5 , headers = self.headers)
        videoInfo = re.findall( r'playAddr: "([\S]*?)"',req.text)[0]
        vid = re.findall( r'vid=([\S]*?)&',videoInfo)[0]
        addr = videoInfo.replace("/playwm/","/play/")
        return vid,addr,session

    def __download(self, vid, info, session):
        self.headers['user-agent'] = H1
        videoBin = session.get(info,timeout = 5, headers = self.headers );
        with open('%s.mp4' % (vid),'wb') as fb:
            fb.write(videoBin.content)
        self.headers['user-agent'] = H0
        return "下载完成"

    def run(self, url):
        try:
            self.url = url
            vid,info,session = self.__get_real_url()
            return self.__download(vid, info, session)
        except Exception as e:
            return str(e)