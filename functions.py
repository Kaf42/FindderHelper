import os
import re
import shutil
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.command import Command
from configparser import ConfigParser

target_url = "https://www.imf.org"
time_stamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
config = ConfigParser()
config.read('config.ini')
chrome_address = config['Chrome']['chrome_path']
chromedrive_address = config['Chrome']['chromedriver_path']


def UrlSniffing(url):
    ClearProxyAndChrome()
    # 1.开启代理
    command = "mitmdump -w mitmFile.txt -s proxy_rule.py"
    os.system("start cmd.exe cmd /k " + command)

    # 2.打开浏览器
    driver = CreateChromeDriver()
    driver.get(url)

    try:
        while True:
            if driver.execute(Command.GET_TITLE)['value'] is None:
                break
    except:
        pass
    ClearProxyAndChrome()
    print("浏览器已关闭！进行后续处理。")

    # 3.处理中间文件
    # 读取数据
    with open(r"getUrl.txt", "r") as f:
        get_urls = f.readlines()
    # 转移中间文件
    os.rename("getUrl.txt", "getUrls_" + time_stamp + ".txt")
    shutil.move("getUrls_" + time_stamp + ".txt", r"./tmp/getUrls_" + time_stamp + ".txt")
    # 正则化处理， 正则表达式：[a-zA-Z]+://[^/]*[$/]
    re_urls = []
    re_rules = r"[A-Za-z]+://.+?/"
    for url in get_urls:
        re_url = re.search(re_rules, url).group(0)
        # 去除重复值
        if re_url not in re_urls:
            re_urls.append(re_url)

    # 4.写入结果文件
    with open("./tmp/result_" + time_stamp + ".txt", "w") as f:
        for url in re_urls:
            f.write(url + "\n")
    re_urls = str(re_urls)[2:-2].replace("', '", "\n")
    # print(re_urls)
    return re_urls


def ClearProxyAndChrome():
    # 关闭相关进程
    os.system("taskkill /f /im cmd.exe")
    os.system("taskkill /f /im WindowsTerminal.exe")
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im chromedriver.exe")


def CreateChromeDriver(headless=False):
    """
    :param headless: 是否无头模式
    :return: 谷歌浏览器
    """
    # 启动webdriver配置项
    options = webdriver.ChromeOptions()
    if headless:  # 如果为True，则爬取时不显示浏览器窗口
        options.add_argument('--headless')

    # D:\chrome-win64\chrome.exe --proxy-server = 127.0.0.1:8080 --ignore-certificate-errors
    # 做一些控制上的优化
    options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')  # 忽略SSL报错
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])  # 浏览器规避
    options.add_experimental_option('useAutomationExtension', False)

    #  设置代理
    proxy_ip = '127.0.0.1:8080'
    options.add_argument('--proxy-server=%s' % proxy_ip)
    # 指定chrome的路径
    options.binary_location = chrome_address
    service = Service(chromedrive_address)
    # 创建浏览器对象
    browser = webdriver.Chrome(service=service, options=options)
    # 破解反爬措施
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
    )
    return browser


if __name__ == "__main__":
    UrlSniffing(target_url)
    # ClearProxyAndChrome()
