import cnnScrape
import aljazeeraScrape
import guardianScrape
import apnewsScrape
import cbsScrape
from collections import defaultdict, Counter
import compare
import groqApi

# Combine all articles into one list with source labels and their importance (index)
articles = cnnScrape.articles + aljazeeraScrape.articles + guardianScrape.articles + apnewsScrape.articles + cbsScrape.articles

# Grouping articles based on similarity
grouped_articles = []
while articles:
    curr_article = articles.pop(0)
    group = [curr_article]
    sources_in_group = {curr_article.source}

    i = 0
    while i < len(articles):
        other_article = articles[i]
        title1 = curr_article.title
        title2 = other_article.title
        embeddings = compare.encode_titles(title1, title2)
        similarity = compare.compute_similarity(embeddings)
        if similarity > 0.8:
            articles.pop(i)
            group.append(other_article)
            sources_in_group.add(other_article.source)
        else:
            i += 1
    
    if len(group) > 1:
        grouped_articles.append(group)

# Create a dictionary of intersecting title words for each group and their counts
def get_intersecting_words(group):
    all_words = [article.title_words for article in group]
    word_counts = Counter(word for words in all_words for word in words)
    return word_counts

# Remove duplicate articles within each group
def remove_duplicates(group):
    unique_articles = {}
    for article in group:
        if article.source not in unique_articles:
            unique_articles[article.source] = article
        else:
            if article.importance < unique_articles[article.source].importance:
                unique_articles[article.source] = article
    return list(unique_articles.values())

# Calculate the average ranking value for each group
def calculate_average_importance(group):
    return sum(article.importance for article in group) / len(group)

# Add intersecting words and average importance to each group
grouped_info = []
for i, group in enumerate(grouped_articles):
    group = remove_duplicates(group)
    intersecting_words = get_intersecting_words(group)
    avg_importance = calculate_average_importance(group)
    grouped_info.append((group, intersecting_words, avg_importance))

# Sort groups first by number of articles, then by average importance
grouped_info.sort(key=lambda x: (len(x[0]), -x[2]), reverse=True)

# Return top five groups
top_five_groups = grouped_info[:5]

# Print results
for i, (group, intersecting_words, avg_importance) in enumerate(top_five_groups):
    print(f"Group {i + 1} of articles:")
    for article in group:
        print(f"Source: {article.source}, URL: {article.url}, Title: {article.title}, Importance: {article.importance}")
    print(f"Title: {groqApi.generate_title(intersecting_words)}")
    print(f"Average importance: {avg_importance:.2f}")
    print()  # Add newline for readability
