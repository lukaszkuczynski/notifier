from unittest import TestCase, main
from application.changeobserver import ChangeObserver


class ChangeObserverTest(TestCase):

    def test_it(self):
        params = {
            'input' : {
                'type' : 'url.content',
                "url" : "http://www.timeapi.org/utc/now?format=%25a%20%25b%20%25d%20%25I:%25M:%25S"
            },
            'stateManager' : {
                'type' : 'file',
                'filename' : '../output/aa.json'
            },
            'comparator' : {
                'type' : 'text'
            },
            'notifier' : {
                'type' : 'debug',
                'recipients' : ['aa@wp.pl']
            }
        }
        c = ChangeObserver(params)
        diff = c.notify_if_changed()
        self.assertIsNotNone(diff)


if __name__ == '__main__' :
    main();