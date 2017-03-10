# coding:utf8
import os
import sys
import platform
from datetime import datetime
import traceback
from json import dumps, loads

class Lock(object):
    
    def __init__(self):
        self.workspace = os.path.abspath(os.path.dirname(__file__))
        self.pid = os.path.join(self.workspace, 'common_call.pid')

    def check(self):
        '''检查进程是否存在
        '''
        if platform.system().lower() == 'linux':
            if os.path.exists(self.pid):
                with open(self.pid, 'rb') as fp:
                    pid = fp.read()
                try: 
                    pid = int(pid)
                except:
                    pid = -1
                return os.path.exists('/proc/%d' % pid)
        else:
            return os.path.exists(self.pid)

        return False

    def acquire(self):
        pid = str(os.getpid())
        with open(self.pid, 'wb') as fp:
            fp.write(pid)

        print datetime.now(), 'create pid(%s) >>> %s' % (pid, self.pid)

    def release(self):
        os.remove(self.pid)
        print datetime.now(), 'remove %s' % self.pid