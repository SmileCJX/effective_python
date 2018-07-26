#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# 从剪贴板中复制和黏贴
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexs in the 'lines' list
    lines[i] = '*' + lines[i] # add start to each string in "lines" list
text = '\n'.join(lines)

pyperclip.copy(text)