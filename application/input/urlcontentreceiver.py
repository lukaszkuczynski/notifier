'''
Created on 21 lut 2016

@author: luk
'''

from application.input.datareceiver import DataReceiver
import requests

class UrlContentReceiver(DataReceiver):
    '''
    classdocs
    '''


    def __init__(self, params=None):
        '''
        Constructor
        '''
        self.url = params['input']['url']
#         self.xpath = params['input']['xpath']
        
    def receive(self):
        r = requests.get(self.url)
        return r.content
        
        
if __name__ == '__main__' :
    params = {
        'input' : {
            'url' : 'http://www.timeapi.org/utc/now'
        }
    }
    rec = UrlContentReceiver(params)
    rec.receive()        
    