import cnnScrape
import aljazeeraScrape
import guardianScrape
from collections import defaultdict
import article
import pandas as pd
import compare

# Combine all articles into one list with source labels and their importance (index)
articles = cnnScrape.articles + aljazeeraScrape.articles 
# + guardianScrape.articles

# Initialize an ArticleForest to hold the grouped articles
article_groups = article.ArticleForest()
viewed_and_grouped = []

def group_similar_articles(article_node, articles):
    i = 0
    while i < len(articles):
        other_article = articles[i]
        other_article_node = article.ArticleNode(other_article)
        title1 = article_node.article.title
        title2 = other_article_node.article.title
        embeddings = compare.encode_titles(title1, title2)
        similarity = compare.compute_similarity(embeddings)
        if similarity > 0.8:
            print(title1, " | ", title2)
            article_node.add_child(other_article_node)
            # Recursively group similar articles for the child article
            articles.pop(i)
            group_similar_articles(other_article_node, articles)
        else:
            i += 1

# Loop through all articles
while articles:
    article_obj = articles.pop(0)
    # Create an article node and tree for the current article
    article_node = article.ArticleNode(article_obj)
    article_tree = article.ArticleTree(article_node)
    
    # Call the group_similar_articles function to group similar articles
    group_similar_articles(article_node, articles)

    if len(article_node.children) > 0:
        article_groups.add_tree(article_tree)

print(len(article_groups.trees))