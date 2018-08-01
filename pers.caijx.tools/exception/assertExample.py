#! python3
# assertExample.py - 断言
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open','The pod bay door need to be "open".'
podBayDoorStatus = 'I\'m sorry,','The pod bay door need to be "open".'
assert podBayDoorStatus == 'open'