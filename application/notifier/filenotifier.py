'''
Created on 21 lut 2016

@author: luk
'''

import os, json
from datetime import datetime

class FileNotifier():
    '''
    classdocs
    '''


    def __init__(self, params=None):
        self.filename = params['notifier']['filename']
        if not os.path.isfile(self.filename) :
            open(self.filename, 'w+')
        
    def notify(self, diff):
        tm = datetime.utcnow()
        f = open(self.filename, 'a')
        f.write(str(tm) +" : " + str(diff['current_state']) + "\n")
        f.close()