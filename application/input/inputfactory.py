'''
Created on 21 lut 2016

@author: luk
'''
from input.urlcontentreceiver import UrlContentReceiver

class InputFactory(object):
    '''
    classdocs
    '''


    def get(self, params):    
        if (params['input']['type'] == 'url.content') :
            return UrlContentReceiver(params)
        