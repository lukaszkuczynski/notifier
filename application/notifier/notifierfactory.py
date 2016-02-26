'''
Created on 21 lut 2016

@author: luk
'''
from notifier.debugnotifier import DebugNotifier
from notifier.filenotifier import FileNotifier
from notifier.mailnotifier import MailNotifier

class NotifierFactory(object):
    '''
    classdocs
    '''


    def get(self, params):    
        if (params['notifier']['type'] == 'debug') :
            return DebugNotifier()
        if (params['notifier']['type'] == 'file') :
            return FileNotifier(params)
        if (params['notifier']['type'] == 'mail') :
            return MailNotifier(params)        