class Article:

    def __init__(self, title, link='', text=''):
        self.title = title
        self.link = link
        self.text = text

    def __str__(self):
        return "ARTICLE " + self.__dict__.__str__()

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.title) ^ hash(self.link) ^ hash(self.text)