#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# 用一个关键字保存剪贴板内容
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve,pyperclip,sys

mcbShelf = shelve.open('.\\mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()

# todo 扩展多重剪贴板，增加一个delte <keyword>命令行参数，它将从shelf中删除一个关键字。然后添加一个delete命令行参数，它将删除所有关键字