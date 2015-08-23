#!/usr/bin/python
# Filename: backup_ver1.py
import os
import time

source = ['/users/allywang/cppcode', '/users/allywang/djcode']

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M')

if not os.path.exists(today):
    os.mkdir(today)
    print 'Succesfully creatd directory', today
print 'os.sep', os.sep

#target = today + os.sep + now + '.zip'
comment = raw_input('Enter a comment --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
            comment.replace(' ', '_') + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

print zip_command

if os.system(zip_command) == 0:
    print 'Successful backup to ', target
else:
    print 'Backup FAILED'

