#!/usr/bin/python 
# -*- coding: utf-8 -*-

from Vibrato import Vibrato


if __name__ == '__main__':
    url = "https://v.douyin.com/nMuYtN/"
    vibrato = Vibrato()
    print(vibrato.run(url))