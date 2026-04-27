from Bio import Entrez

Entrez.email = "your_email@example.com"


def search_pubmed(keyword: str, max_results: int = 5) -> list[str]:
    """
    PubMedでキーワード検索をして、論文IDのリストを返す関数。

    keyword:
        検索語。例: "cancer immunotherapy"

    max_results:
        最大で何件取得するか。

    戻り値:
        PubMed IDのリスト。
        例: ["12345678", "23456789"]
    """

    handle = Entrez.esearch(
        db="pubmed",
        term=keyword,
        retmax=max_results,
        sort="relevance"
    )

    record = Entrez.read(handle)
    handle.close()

    return record["IdList"]


def fetch_article_details(pubmed_ids: list[str]) -> list[dict]:
    """
    PubMed IDのリストを受け取り、論文情報を取得する関数。

    pubmed_ids:
        PubMed IDのリスト。

    戻り値:
        論文情報の辞書を入れたリスト。
    """

    if len(pubmed_ids) == 0:
        return []

    handle = Entrez.efetch(
        db="pubmed",
        id=",".join(pubmed_ids),
        rettype="xml",
        retmode="xml"
    )

    records = Entrez.read(handle)
    handle.close()

    articles = []

    for article in records["PubmedArticle"]:
        medline = article["MedlineCitation"]
        article_data = medline["Article"]

        title = str(article_data.get("ArticleTitle", "No title"))

        abstract_parts = article_data.get("Abstract", {}).get("AbstractText", [])
        abstract = " ".join(str(part) for part in abstract_parts)

        journal = article_data.get("Journal", {})
        journal_title = str(journal.get("Title", "Unknown journal"))

        pub_date = journal.get("JournalIssue", {}).get("PubDate", {})
        year = str(pub_date.get("Year", "Unknown year"))

        authors = article_data.get("AuthorList", [])
        author_names = []

        for author in authors[:5]:
            last_name = author.get("LastName", "")
            fore_name = author.get("ForeName", "")
            full_name = f"{fore_name} {last_name}".strip()

            if full_name:
                author_names.append(full_name)

        articles.append(
            {
                "title": title,
                "abstract": abstract,
                "journal": journal_title,
                "year": year,
                "authors": author_names,
            }
        )

    return articles