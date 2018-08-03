#! python3
# baidu.py - Lauches a map in the browser using an address from the
# command line or clipboard.
import webbrowser,sys,pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    keyName = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    keyName = pyperclip.paste()

webbrowser.open('http://www.baidu.com/s?wd=' + keyName)