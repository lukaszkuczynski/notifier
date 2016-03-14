import unittest

from application.comparator.listcomparator import ListComparator
from application.model.article import Article


class ListComparatorTestCase(unittest.TestCase):

    def assert_diff_empty_list(self, diff):
        self.assertTrue(diff.value == [])

    def assert_diff_has_elements(self, diff):
        self.assertTrue(diff.changed())

    def test_returns_no_diff_for_empty(self):
        sut = ListComparator()
        prev = []
        curr = []
        diff = sut.compare(prev, curr)
        self.assert_diff_empty_list(diff)

    def test_returns_diff_for_1st_empty_2nd_notempty(self):
        sut = ListComparator()
        prev = []
        curr = ['1']
        diff = sut.compare(prev, curr)
        self.assert_diff_has_elements(diff)
        self.assertListEqual(diff.value, ['1'])

    def test_diff_has_list_with_order(self):
        sut = ListComparator()
        prev = range(1,9)
        curr = range(1,11)
        diff = sut.compare(prev, curr)
        self.assert_diff_has_elements(diff)
        self.assertListEqual(diff.value, [9,10])

    def getArticles(self, count):
        articles = []
        for n in range(1, count+1) :
            articles.append(self.getArticle(n))
        return articles

    def getArticle(self, no):
        a = {}
        a['title'] = 'title '+str(no)
        a['link'] = 'link '+str(no)
        a['text'] = 'text '+str(no)
        return Article(a['title'], a['link'], a['text'])

    def test_diff_is_empty_when_objects_equal(self):
        sut = ListComparator()
        prev = self.getArticles(2)
        curr = self.getArticles(2)
        diff = sut.compare(prev, curr)
        self.assert_diff_empty_list(diff)

    def test_diff_is_not_empty_when_more_objects(self):
        sut = ListComparator()
        prev = self.getArticles(2)
        curr = self.getArticles(3)
        diff = sut.compare(prev, curr)
        self.assert_diff_has_elements(diff)

    def test_diff_has_only_one_element_which_differs(self):
        sut = ListComparator()
        prev = self.getArticles(2)
        curr = self.getArticles(3)
        diff = sut.compare(prev, curr)
        self.assert_diff_has_elements(diff)
        art = diff.first_element()
        self.assertEqual(art, self.getArticle(3))
        self.assert_diff_has_elements(diff)

    def test_diff_has_only_one_element_which_was_added_not_one_which_is_lacking(self):
        sut = ListComparator()
        prev = self.getArticles(2)
        prev.insert(0, self.getArticle(23))
        curr = self.getArticles(3)
        diff = sut.compare(prev, curr)
        self.assert_diff_has_elements(diff)
        art = diff.first_element()
        self.assertEqual(art, self.getArticle(3))
        self.assert_diff_has_elements(diff)


if __name__ == '__main__':
    unittest.main()
