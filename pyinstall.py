#!/usr/bin/python 
# -*- coding: utf-8 -*-
import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['Vibrato.py','-w','-F','--icon=favicon.ico']
    run(opts)
