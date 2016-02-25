'''
Created on 21 lut 2016

@author: luk
'''

from lxml import html
import requests

class WebElementReceiver():
    '''
    classdocs
    '''


    def __init__(self, params=None):
        self.url = params['input']['url']
        self.xpath = params['input']['xpath']
        
    def receive(self):
        page = requests.get(self.url)
        tree = html.fromstring(page.content)
        val = tree.xpath(self.xpath)
        if len(val) == 0 :
            raise Exception("value under "+ self.url + " xpath " + self.xpath + "not found!")
#         if len(val) > 1 :
#             raise Exception("found more than 1 "+ self.url + " xpath " + self.xpath + "not found!")
        return val[0]


if __name__ == '__main__' :
    
    url = 'http://www.bbc.com/news'
    xpath = '//*[@id="comp-top-story-1"]/div/div/a[1]/h3/span/text()'
    
    params = { 
                'input' : {
                'type' : 'web.element',
                'url' : url,
                'xpath' : xpath  
                
            }
              };

    w = WebElementReceiver(params)
    print(w.receive())