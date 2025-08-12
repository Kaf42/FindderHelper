import os

from mitmproxy import ctx


# 所有发出的请求数据包都会被这个方法所处理,这里只是打印一下一些项；当然可以修改这些项的值直接给这些项赋值即可
def request(flow):
    request = flow.request  # 获取请求对象
    info = ctx.log.info  # 实例化输出类
    # 打印请求的url、请求方法、host头、请求端口、所有请求头部、cookie头
    # content = " ".join([request.url, request.method, request.host, str(request.port), str(request.headers), str(request.cookies)])
    # content = " ".join([request.url, request.method, request.host, str(request.port)])
    # info(content)
    info(request.url)
    # 判断文件夹是否存在
    if not os.path.isdir('tmp'):
        os.mkdir('tmp')
    with open(r"getUrl.txt", "a") as f:
        f.write(request.url + "\n")


# 所有服务器响应的数据包都会被这个方法处理
def response(flow):
    # 获取响应对象
    response = flow.response
    # 实例化输出类
    info = ctx.log.info
    # 打印响应码、所有头部、cookie头部、响应报文内容
    # content = " ".join([str(response.status_code), str(response.headers), str(response.cookies),str(response.text)])
    # info(content)
