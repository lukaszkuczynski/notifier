import unittest
from notifier.mailnotifier import MailNotifier
from model.diff import Diff
from model.article import Article

class ListComparatorTestCase(unittest.TestCase):

    def test_mail_msg_raw(self):
        sut = MailNotifier()
        sut.recipients = []
        mail_config = {
            'subject':'subby',
            'from' : 'from_mer'
        }
        diff = 'zz'
        msg = sut.build_msg_raw(diff, mail_config)
        print(msg)

    def test_mail_msg_html(self):
        sut = MailNotifier()
        sut.recipients = []
        mail_config = {
            'subject':'subby',
            'from' : 'from_mer'
        }
        art = Article('tit')
        art2 = Article('titł')
        diff = Diff([art,art2])
        # template = '<body>hello</body>'
        template = 'd://temp//articles.html'
        msg = sut.build_msg_html(diff.all_changes(), mail_config, template)
        print(msg)