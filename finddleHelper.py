from PyQt5.QtWidgets import QMainWindow, QHeaderView, QAbstractItemView
import PyQt5.QtGui as QtGui
import logging
import win32clipboard as wcb
import win32con as wc

from mainwindow import Ui_FinddleHelper
from functions import UrlSniffing

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)


class FinddleHelper(QMainWindow, Ui_FinddleHelper):
    def __init__(self, parent=None):
        super(FinddleHelper, self).__init__(parent)
        self.InitUI()

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
        # self.tableWidget.horizontalHeader().resizeSection(0, 100)
        # self.tableWidget.horizontalHeader().resizeSection(1, 100)
        # self.tableWidget.horizontalHeader().resizeSection(2, 400)
        # 设置列宽自适应
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 绑定按钮与信号槽
        self.button_start.clicked.connect(self.ButtonStartClicked)
        self.button_copy.clicked.connect(self.ButtonCopyClicked)
        self.button_reset.clicked.connect(self.ButtonResetClicked)

        self.urls = "1111111111"


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
        logging.info("url为："+target_url)
        logging.info("开始进行抓包！")
        # 网址嗅探
        urls = UrlSniffing(target_url)
        logging.info("抓包完成！")
        # 网址写入
        for url in urls:
            self.tableInsert(url, 'Get', '200')
        logging.info("插入完成！")
        self.urls = str(urls)
        logging.info(self.urls)

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
        logging.info("copy clicked")
        # 复制至剪切板
        wcb.OpenClipboard() # 打开剪切板
        wcb.EmptyClipboard()    # 清空剪切板
        wcb.SetClipboardData(wc.CF_TEXT, self.urls.encode('gbk'))   # 写入剪贴板
        wcb.CloseClipboard()    # 关闭剪切板


    def ButtonResetClicked(self):
        """
        重置按钮功能实现
        :return:
        """
        logging.info("reset clicked")
        self.urls = ""
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
