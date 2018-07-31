#! python3
# 创建和添加到zip文件
import zipfile
newZip = zipfile.ZipFile('.\\new.zip','w')
newZip.write('.\\spam.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()