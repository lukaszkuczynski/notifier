import unittest
from application.changeobserver import ChangeObserver


class ChangeObserverArticlesTest(unittest.TestCase):

    def test_get_articles(self):
        params = {
            'input': {
                'type': 'web.element',
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


    def observer_takes_article_and_mutates_test(self):
        params = {
            "input": {
                "type" : "web.element",
                "url" : "http://www.domiporta.pl/sprzedam-dzialke-dolnoslaskie_sroda_slaska?LocalizationId=51620",
                "element": {
                    "parentPath":"div.WynikiLista div.NoweWyniki",
                    "keys": {
                        "title": ["div.Tytul a.TytulOgloszenia"],
                        "price": ["span.CenaTekst"]
                    }
                }
            },
            "mutate": {
                "key": {
                    "price" : "whitespace"
                }
            },
            "stateManager" : {
                "type" : "raw",
                "filename" : "articles.txt"
            },
            "comparator" : {
                "type" : "list"
            },
            "notifier" : {
                    "type" : "mail",
                    "recipients" : ["kuczynskilukasz@gmail.com"],
                    "template" : "d://prj//notifier//mail_templates//offer.html"
            }
        }
        observer = ChangeObserver(params)
        observer.notify_if_changed()


