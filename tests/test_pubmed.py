from pubmed_client import search_pubmed, fetch_article_details


ids = search_pubmed("cancer immunotherapy", max_results=3)
print(ids)

articles = fetch_article_details(ids)

for article in articles:
    print("--------")
    print(article["title"])
    print(article["year"])
    print(article["journal"])
    print(article["abstract"][:300])