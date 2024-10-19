from abc import ABC, abstractmethod


class Post(ABC):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_text(self):
        pass


class Link(Post):
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def get_title(self):
        return self.title

    def get_text(self):
        return self.url


class Comment(Post):
    def __init__(self, title, comment, user):
        self.title = title
        if len(comment) > 500:
            raise ValueError("Comment is too long.")
        self.comment = comment
        self.user = user

    def get_title(self):
        return self.title

    def get_text(self):
        return self.comment

    def get_user(self):
        return self.user


class Article(Post):
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def get_title(self):
        return self.title

    def get_text(self):
        return self.body


if __name__ == "__main__":
    posts = []
    a = Link("Link Title", "http://example.com/link.html")
    posts.append(a)
    print(a.get_text(),"\n")

    b = Comment("Comment Title", "comment", "Nitesh")
    c = Article("Article Title", "Article Text")
    posts.append(b)
    posts.append(c)
    for p in posts:
        print(p.get_title(), "\t: ", p.get_text())
