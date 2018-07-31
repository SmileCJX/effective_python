#! python3
# 永久删除文件和文件夹
# os.unlink(path) 删除path处的文件
# os.rmdir(path) 删除path处的文件夹。该文件夹必须为空，其中没有任何文件和文件夹
# shutil.rmtree(path) 将删除path处的文件夹，它包含的所有文件和文件夹都会被删除

import os
for filename in os.listdir():
    if filename.endswith('.jpg'):
        os.unlink(filename)
        # 先显示会被删除的文件
        # print(filename)