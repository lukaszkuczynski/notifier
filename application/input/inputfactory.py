'''
Created on 21 lut 2016

@author: luk
'''
from input.urlcontentreceiver import UrlContentReceiver
from input.web_element_receiver import WebElementReceiver

class InputFactory(object):
    '''
    classdocs
    '''


    def get(self, params):    
        if (params['input']['type'] == 'url.content') :
            return UrlContentReceiver(params)
        if (params['input']['type'] == 'web.element') :
            return WebElementReceiver(params)
        