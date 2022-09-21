from .details import Details

class Document:

    def __init__(self, idx, title, contents, date):
        self.id = idx
        self.title = title
        self.contents: list = contents
        self.details = Details(date)


    def get_url(self):
        return self.url

    def set_contents(self, contents):
        self.contents = contents

    def set_date(self, date):
        self.date = date

    def set_id(self, idx):
        self.id = idx

    def set_url(self, url):
        self.url = url

    def set_title(self, title):
        self.title = title

    def set_content(self, content):
        self.contents = content

    def set_author(self, author):
        self.author = author

    def similar(self, article):
        return self.title == article.title

    def __str__(self):
        return "Article:" + str(self.id) + str(self.author) + str(self.title) + str(self.url) + str(
            self.contents) + str(self.date)
class Article:

    def __init__(self, idx, url, title, contents, date, author):
        self.id = idx
        self.url = url
        self.title = title
        self.contents = contents
        self.date = date
        self.author = author

    def get_url(self):
        return self.url

    def set_contents(self, contents):
        self.contents = contents

    def set_date(self, date):
        self.date = date

    def set_id(self, idx):
        self.id = idx

    def set_url(self, url):
        self.url = url

    def set_title(self, title):
        self.title = title

    def set_content(self, content):
        self.contents = content

    def set_author(self, author):
        self.author = author

    def similar(self, article):
        return self.title == article.title

    def __str__(self):
        return "Article:" + str(self.id) + str(self.author) + str(self.title) + str(self.url) + str(
            self.contents) + str(self.date)
