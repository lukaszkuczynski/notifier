import unittest
from application.model.diff import Diff
from application.model.article import Article

class DiffTest (unittest.TestCase):

    def test_diff_str(self):
        art1 = Article('title 1')
        art2 = Article('tit 2')
        df = Diff([art1,art2])
        print(df)

