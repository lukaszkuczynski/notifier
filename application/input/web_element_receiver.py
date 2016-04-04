'''
Created on 21 lut 2016

@author: luk
'''

from lxml import html
import requests
from model.element import Element


class WebElementReceiver:
    '''
    Receives web articles from page
    '''


    def __init__(self, params=None):
        self.url = params['input']['url']
        self.element_parent = params['input']['element']['parentPath']
        self.element_keys = params['input']['element']['keys']

    def parse_from_element_using_css(self, element, cssselects):
        for select in cssselects :
            title_candidate = element.cssselect(select)
            if len(title_candidate) == 1 :
                if title_candidate[0].text:
                    return title_candidate[0].text
        return ''

    def receive(self):
        elements = []
        page = requests.get(self.url)
        page_tree = html.fromstring(page.content)
        element_nodes = page_tree.cssselect(self.element_parent)
        for element_node in element_nodes:
            element = Element()
            for key in self.element_keys:
                path = self.element_keys[key]
                element_value = self.parse_from_element_using_css(element_node, path)
                element.add_key_value(key, element_value)
            elements.append(element)
        return elements

