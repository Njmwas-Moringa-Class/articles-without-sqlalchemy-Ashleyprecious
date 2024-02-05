# Author.py
from Article import Article  # Import the Article class

class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.authored_articles = []
        self.__class__.all_authors.append(self)

    def __str__(self):
        return f"Author: {self.name}"

    @property
    def articles(self):
        return self.authored_articles

    @property
    def magazines(self):
        return list(set(article.magazine for article in self.authored_articles))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self.authored_articles.append(new_article)

    @property
    def topic_areas(self):
        return list(set(article.magazine.category for article in self.authored_articles))
