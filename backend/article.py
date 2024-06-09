class Article:
    def __init__(self, source, importance, url, title, title_words, img_source):
        self.source = source
        self.importance = importance
        self.url = url
        self.title = title
        self.title_words = title_words
        self.img_source = img_source

    def __repr__(self):
        return f"Source: {self.source}, Importance: {self.importance}, URL: {self.url}, Title: {self.title}, Title Words: {self.title_words}, Image: {self.img_source}"


class ArticleNode:
    def __init__(self, article):
        self.article = article
        self.children = []

    def add_child(self, child_article_node):
        self.children.append(child_article_node)


class ArticleTree:
    def __init__(self, root_node):
        self.root = root_node

    def add_child(self, parent_node, child_article):
        parent_node.add_child(child_article)


class ArticleForest:
    def __init__(self):
        self.trees = []

    def add_tree(self, tree):
        self.trees.append(tree)

