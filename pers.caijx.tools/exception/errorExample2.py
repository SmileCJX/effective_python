#! python3
# errorExample2.py - 将错误信息写入日志文件
import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('.\\errorInfo.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceBack info was written to errorInfo.txt.')