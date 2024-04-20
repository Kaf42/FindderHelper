import logging

import PyQt5.QtGui as QtGui
from PyQt5.QtWidgets import QMainWindow, QAbstractItemView

from mainwindow import Ui_FinddleHelper
from thread import Thread_Copy, Thread_Sniffer

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)


class Finddle_Helper(QMainWindow, Ui_FinddleHelper):
    def __init__(self, parent=None):
        super(Finddle_Helper, self).__init__(parent)
        self.InitUI()
        self.urls = "www.baidu.com;\nwww.baidu.com111"

    def InitUI(self):
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("resource/icon.ico"))  # 设置图标

        # 设置网址表格
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格字体加粗
        font = self.tableWidget.horizontalHeader().font()
        font.setBold(True)
        self.tableWidget.horizontalHeader().setFont(font)
        # 手动设置列宽
        self.tableWidget.horizontalHeader().resizeSection(0, 470)
        self.tableWidget.horizontalHeader().resizeSection(1, 50)
        self.tableWidget.horizontalHeader().resizeSection(2, 50)
        # 设置列宽自适应
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 绑定按钮与信号槽
        self.button_start.clicked.connect(self.ButtonStartClicked)
        self.button_copy.clicked.connect(self.ButtonCopyClicked)
        self.button_reset.clicked.connect(self.ButtonResetClicked)

    def ButtonStartClicked(self):
        """
        开始按钮功能实现
        :return:
        """
        logging.info("start clicked")
        # 获取目标网址
        target_url = self.lineEdit.text()
        if target_url == "":
            logging.info("url为空！")
            return
        logging.info("url为：" + target_url)
        logging.info("开始进行抓包！")

        self.button_start.setEnabled(False)
        try:
            self.thread_start = Thread_Sniffer(target_url, self.tableWidget)
            self.thread_start.finishSignal.connect(lambda: self.button_start.setEnabled(True))
            self.thread_start.urlsSignal.connect(lambda: self.button_start.setEnabled(True))
            self.thread_start.urlsSignal.connect(self.set_urls)
            self.thread_start.start()
            logging.info(self.urls)
        except Exception as e:
            print(e)

    def set_urls(self, urls):
        self.urls = urls

    def tableInsert(self, url, type, status):
        """
        表格数据插入
        :param url:网址
        :param type: 类型
        :param status: 状态
        :return:
        """
        self.tableWidget.insertRow(self.tableWidget.rowCount(), 1, url)
        self.tableWidget.insertRow(self.tableWidget.rowCount(), 1, type)
        self.tableWidget.insertRow(self.tableWidget.rowCount(), 1, status)

    def ButtonCopyClicked(self):
        """
        复制按钮功能实现
        :return:
        """
        logging.info("copy clicked!")
        self.thread_copy = Thread_Copy(self.urls)  # 创建线程
        self.thread_copy.start()

    def ButtonResetClicked(self):
        """
        重置按钮功能实现
        :return:
        """
        logging.info("reset clicked")
        self.urls = ""
        self.lineEdit.clear()
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
