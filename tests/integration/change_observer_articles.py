import unittest
from application.changeobserver import ChangeObserver
from config import config

class ChangeObserverArticlesTest(unittest.TestCase):

    def test_get_articles(self):

        recipients = config.config()['mail']['default_recipients']
        params = {
            'input': {
                'type': 'web.articles',
                'url': 'http://wiadomosci.wp.pl/?ticaid=1169c4&_ticrsn=3',
                'article': {
                    'path':'ul.wiadomosciLst li',
                },
                'articleElement': {
                    'titles': ['h2 a', 'a'],
                    'contents': ['h2 a', 'a'],
                    'link':['']
                }
            },
            'stateManager' : {
                'type' : 'raw',
                'filename' : '../../output/art.txt'
            },
            'comparator' : {
                'type' : 'list'
            },
            'notifier' : {
                'type' : 'debug',
            }
        }
        observer = ChangeObserver(params)
        observer.notify_if_changed_new_diff()

