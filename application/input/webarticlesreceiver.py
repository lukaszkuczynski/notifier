'''
Created on 21 lut 2016

@author: luk
'''

from lxml import html
import requests
from application.model.article import Article


class WebArticlesReceiver:
    '''
    Receives web articles from page
    '''


    def __init__(self, params=None):
        self.url = params['input']['url']
        self.articles_path = params['input']['article']['path']
        self.titles = params['input']['articleElement']['titles']
        self.contents = params['input']['articleElement']['contents']

    def parse_from_element_using_css(self, element, cssselects):
        for select in cssselects :
            title_candidate = element.cssselect(select)
            if len(title_candidate) == 1 :
                if title_candidate[0].text:
                    return title_candidate[0].text
        return ''

    def receive(self):
        articles = []
        page = requests.get(self.url)
        page_tree = html.fromstring(page.content)
        articles_nodes = page_tree.cssselect(self.articles_path)
        for article_node in articles_nodes:
            title = self.parse_from_element_using_css(article_node, self.titles)
            content = self.parse_from_element_using_css(article_node, self.contents)
            a = Article(title=title, text=content)
            print(a)
            articles.append(a)
        return articles


if __name__ == '__main__':
    
    url = 'http://wiadomosci.wp.pl/?ticaid=1169c4&_ticrsn=3'
    article = 'ul.wiadomosciLst li'
    titles = ['h2 a', 'a']
    contents = titles
    link = ''
    params = { 
        'input': {
            'type': 'web.element',
            'url': url,
            'article': {
                'path':article,
            },
            'articleElement': {
                'titles':titles,
                'contents':contents,
                'link':link,
            }
        }
    };

    w = WebArticlesReceiver(params)
    print(w.receive())