import unittest
from application.changeobserver import ChangeObserver


class ChangeObserverArticlesTest(unittest.TestCase):

    def test_get_articles(self):
        params = {
            'input': {
                'type': 'web.articles',
                'url': 'http://wiadomosci.wp.pl/?ticaid=1169c4&_ticrsn=3',
                'element': {
                    'parentPath':'div#bxWiadPolska ul.wiadomosciLst li',
                    'keys': {
                        'title': ['h2 a', 'a'],
                        'content': ['h2 a', 'a'],
                    }
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

