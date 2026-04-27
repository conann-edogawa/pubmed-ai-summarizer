import streamlit as st

from pubmed_client import search_pubmed, fetch_article_details
from summarizer import summarize_article


st.set_page_config(
    page_title="PubMed論文要約AIツール",
    page_icon="🧬",
    layout="wide"
)

st.title("PubMed論文要約AIツール")
st.write("キーワードを入力すると、PubMedから関連論文を取得します。")


# 初回だけ保存箱を作る
if "articles" not in st.session_state:
    st.session_state.articles = []


keyword = st.text_input(
    "検索キーワード",
    value="cancer immunotherapy"
)

max_results = st.slider(
    "取得する論文数",
    min_value=1,
    max_value=10,
    value=5
)


# 検索ボタン
if st.button("検索する"):
    with st.spinner("PubMedから論文を取得しています..."):
        ids = search_pubmed(keyword, max_results=max_results)
        articles = fetch_article_details(ids)

        st.session_state.articles = articles


# 保存された論文一覧を表示
if st.session_state.articles:

    st.success(f"{len(st.session_state.articles)}件の論文を取得しました。")

    for index, article in enumerate(st.session_state.articles, start=1):

        st.subheader(f"{index}. {article['title']}")

        st.write(f"**Journal:** {article['journal']}")
        st.write(f"**Year:** {article['year']}")
        st.write(f"**Authors:** {', '.join(article['authors'])}")

        with st.expander("Abstractを見る"):
            st.write(article["abstract"])

        if st.button("この論文を要約する", key=f"sum_{index}"):

            with st.spinner("AIで要約しています..."):

                summary = summarize_article(
                    title=article["title"],
                    abstract=article["abstract"]
                )

            st.markdown("### 日本語要約")
            st.write(summary)

        st.divider()