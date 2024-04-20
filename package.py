# coding=utf-8

import os
import shutil
# from tool_function import wheel


def main():
    # 创建安装包文件夹
    package_dir = r'./FindderHelper_package/'
    package_name = 'FindderHelper'
    zip_name = 'FindderHelper_package'
    try:
        os.mkdir(package_dir)
    except FileExistsError:
        # 获取该文件夹下的所有文件名列表
        del_file(package_dir)

    # 打包
    os.system('pyinstaller -F -w -n '+package_name+' main.py'+' --distpath '+package_dir)

    # 移动文件
    # shutil.copyfile(r'./icnet_publish_data.xlsx', package_dir+'/icnet_publish_data.xlsx')
    shutil.copyfile(r'./config.ini', package_dir+'/config.ini')
    shutil.copyfile(r'./readme.md', package_dir+'/readme.md')
    # shutil.copyfile(r'./icnet_publish.bat', package_dir+'/icnet_publish.bat')
    shutil.copytree(r'./resource', package_dir+'/resource')
    # 删除打包文件
    shutil.rmtree(r'./build')
    os.remove(package_name+'.spec')

    # # 压缩
    # wheel.zip_dir(package_dir, zip_name)


def del_file(path):
    if not os.listdir(path):
        print('目录为空！')
    else:
        for i in os.listdir(path):
            path_file = os.path.join(path, i)  # 取文件绝对路径
            print(path_file)
            if os.path.isfile(path_file):
                os.remove(path_file)
            else:
                del_file(path_file)
                shutil.rmtree(path_file)


if __name__ == '__main__':
    main()