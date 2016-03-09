'''
Created on 21 lut 2016

@author: luk
'''
from input.urlcontentreceiver import UrlContentReceiver
from input.webelementreceiver import WebElementReceiver
from input.webarticlesreceiver import WebArticlesReceiver

class InputFactory(object):
    '''
    classdocs
    '''


    def get(self, params):    
        if (params['input']['type'] == 'url.content') :
            return UrlContentReceiver(params)
        if (params['input']['type'] == 'web.element') :
            return WebElementReceiver(params)
        if (params['input']['type'] == 'web.articles') :
            return WebArticlesReceiver(params)
        