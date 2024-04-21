# -*- coding: utf-8 -*-
import time
from PyQt5.QtCore import QThread, pyqtSignal, QMutex, Qt
import logging

from PyQt5.QtWidgets import QTableWidgetItem

from functions import UrlSniffing
import pyperclip


# 抓包线程
class Thread_Sniffer(QThread):
    # 自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal()
    urlsSignal = pyqtSignal(str)

    # 带一个参数t
    def __init__(self, url, tableWidget):
        super().__init__()
        self.url = url
        self.tableWidget = tableWidget

    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        # 网址嗅探
        print(self.url)
        try:
            urls = UrlSniffing(self.url)
        except Exception as e:
            print(e)
            return
        logging.info("抓包完成！")
        logging.info("获取到的网址为：\n" + urls)
        self.finishSignal.emit()
        self.urlsSignal.emit(urls)
        # 网址写入
        try:
            for url in urls.split('\n'):
                self.tableInsert(url, 'Get', '200')
        except Exception as e:
            logging.error("网址写入表格失败：" + str(e))
        logging.info("插入完成！")

    def tableInsert(self, url, type, status):
        """
        表格数据插入
        :param url:网址
        :param type: 类型
        :param status: 状态
        :return:
        """
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(url))
        self.tableWidget.item(self.tableWidget.rowCount() - 1, 0).setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(type))
        self.tableWidget.item(self.tableWidget.rowCount() - 1, 1).setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(status))
        self.tableWidget.item(self.tableWidget.rowCount() - 1, 2).setTextAlignment(Qt.AlignCenter)


# 定义一个线程类
class Thread_Copy(QThread):
    # 创建线程锁
    qmut = QMutex()

    def __init__(self, urls):
        super().__init__()
        self.urls = urls

    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        self.qmut.lock()  # 加锁
        # wcb.OpenClipboard() # 打开剪切板
        # wcb.EmptyClipboard()    # 清空剪切板
        # wcb.CloseClipboard()    # 关闭剪切板
        pyperclip.copy(self.urls)
        self.qmut.unlock()  # 解锁
