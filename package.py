import os
import shutil  # 导入移动模块

def zip_dir(dir_path, zip_name):
    import zipfile
    zip = zipfile.ZipFile(zip_name + '.zip', "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dir_path):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dir_path, zip_name + '/')
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()

# 创建安装包文件夹
package_dir = r'./FindderHelper/'
package_name = 'FindderHelper'
zip_name = 'FindderHelper'
try:
    # pass
    os.mkdir(package_dir)
except FileExistsError:
    # 获取该文件夹下的所有文件名列表
    file_list = os.listdir(package_dir)

    # 遍历文件列表并删除每个文件
    for file in file_list:
        # 构建完整的文件路径
        file_path = os.path.join(package_dir, file)

        if os.path.isfile(file_path):
            # 如果是文件则直接删除
            os.remove(file_path)

# 打包
os.system(r'D:\Anaconda\Scripts\pyinstaller.exe -F -w -n '+package_name+' WebCrawlerApp.py --distpath ' + package_dir)

# 移动文件
shutil.copyfile(r'./web_crawler_config.json', package_dir+'/web_crawler_config.json')
shutil.copyfile(r'./README.md', package_dir+'/README.md')
shutil.copyfile(r'./proxy_rule.py', package_dir+'/proxy_rule.py')
# 删除打包文件
shutil.rmtree(r'./build')
os.remove(package_name+'.spec')

# # 压缩
zip_dir(package_dir, zip_name)


