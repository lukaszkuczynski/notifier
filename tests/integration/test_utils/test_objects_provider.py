from model.article import Article
from model.diff import Diff


class TestProvider:

    @staticmethod
    def get_articles_diff(art_names):
        articles = []
        for art_name in art_names:
            link = "http://google.pl/search?q="+art_name
            text = "this is text in art "+art_name
            articles.append(Article(title=art_name, link=link, text=text))
        return Diff(articles)