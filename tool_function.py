import os
import sys

import requests
from config import *

class wheel:
    def __init__(self):
        pass

    def send_result(wxsend_key, result):
        """
        微信通知发布
        """
        api = "https://sc.ftqq.com/" + str(wxsend_key) + ".send"
        data = {
            "text": result
        }
        try:
            req = requests.post(api, data=data)
            if req.status_code == 200:
                print("通知发送成功")
            else:
                print("通知发送失败")
        except Exception as e:
            print("通知发送失败:"+str(e))


    # 多线程实现，解决等待期间无响应问题
    @staticmethod
    def thread_it(func, *args):
        """
        多线程实现，解决等待期间无响应问题
        :param func: 线程函数
        :param args: 线程函数的相关参数
        """
        import threading
        t = threading.Thread(target=func, args=args)  # 创建
        t.setDaemon(True)  # 守护
        t.start()  # 启动

    # 重启程序
    @staticmethod
    def restart_program():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    # 压缩指定文件夹
    @staticmethod
    def zip_dir(dir_path, zip_name):
        import zipfile
        zip = zipfile.ZipFile(zip_name + '.zip', "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dir_path):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(dir_path, zip_name + '/')
            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()

    @staticmethod
    def create_chrome_driver(chrome_path, chromedriver_path, headless=False):
        """
        :param chrome_path: 谷歌浏览器位置
        :param chromedriver_path: 谷歌驱动位置
        :param headless: 是否无头模式
        :return: 谷歌浏览器
        """
        from selenium import webdriver
        # 启动webdriver配置项
        options = webdriver.ChromeOptions()
        if headless:  # 如果为True，则爬取时不显示浏览器窗口
            options.add_argument('--headless')

        # 做一些控制上的优化
        options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')  # 忽略SSL报错
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])  # 浏览器规避
        options.add_experimental_option('useAutomationExtension', False)
        # 指定chrome的路径
        options.binary_location = chrome_path
        # 创建浏览器对象
        print(chrome_path, chromedriver_path)
        browser = webdriver.Chrome(chromedriver_path, chrome_options=options)
        # 破解反爬措施
        browser.execute_cdp_cmd(
            'Page.addScriptToEvaluateOnNewDocument',
            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
        )
        return browser

    def write_config():
        from configparser import ConfigParser

        # 创建配置解析器
        config = ConfigParser()

        # 读取配置文件
        config.read('config.ini')

        # 写入配置
        config['DEFAULT']['serveraliveinterval'] = '60'

        # 添加一个新的section
        config['Chrome'] = {}
        config['Chrome']['chrome_path'] = 'D:\chrome-win64\chrome.exe'
        config['Chrome']['chromedriver_path'] = r'D:\Python37\chromedriver.exe'
        config['Chrome']['wxsend_key'] = r'SCT131900TieUhx4Nuj3QQZMfpk7jTdAC9'

        # 写入修改到文件
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        # 再次读取验证修改
        config.read('config.ini')
        print(config['Chrome']['chrome_path'])
        print(config['Chrome']['chromedriver_path'])
        print(config['Chrome']['wxsend_key'])
