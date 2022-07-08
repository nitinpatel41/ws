import os
import time

source = ['/Users/swa/notes']
target_dir = '/Users/swa/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
print(now)
comment = input('Enter a comment --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'