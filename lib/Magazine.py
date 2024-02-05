# Magazine.py

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.additional_info = {}
        self.published_articles = []
        self.__class__.all_magazines.append(self)

    def __str__(self):
        return f"Magazine: {self.name}, Category: {self.category}, Additional Info: {self.additional_info}"

    @property
    def contributors(self):
        return list(set(article.author for article in self.published_articles))

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls.all_magazines if magazine.name == name), None)

    @property
    def article_titles(self):
        return [article.title for article in self.published_articles]

    def contributing_authors(self):
        authors_count = {}
        for article in self.published_articles:
            author = article.author
            authors_count[author] = authors_count.get(author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]

    def update_info(self, key, value):
        self.additional_info[key] = value


