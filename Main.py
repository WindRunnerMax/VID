#!/usr/bin/python 
# -*- coding: utf-8 -*-
# pyuic5 form.ui -o form.py

import re
import sys
from Vibrato import Vibrato
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui
from Form import Ui_Form


class Main(QDialog,Ui_Form):
    """docstring for Vibrato"""
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.vibrato = Vibrato()


    def run(self):
        self.label.setText("稍等")
        QApplication.processEvents()
        url = self.lineEdit.text()
        if url == "":
            self.label.setText("链接不能为空")
        else :
            regx=r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+" 
            listurl=re.findall(regx, url)
            if len(listurl) == 0:
                self.label.setText("解析链接失败")
            else:
                result = self.vibrato.run(listurl[0])
                self.label.setText(str(result))
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dlg=Main()
    dlg.show()
    sys.exit(app.exec_())
