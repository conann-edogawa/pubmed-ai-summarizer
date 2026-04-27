# PubMed論文要約AIツール

PubMedから生命科学・医学論文を検索し、OpenAI APIを用いて日本語要約するWebアプリです。

## 背景

生命科学系学生として、英語論文を素早く理解する課題が多く、
学習効率化のために開発しました。

## 主な機能

- PubMed論文検索
- タイトル / 著者 / 雑誌名 / 年の表示
- Abstract表示
- AIによる日本語要約

## 使用技術

- Python
- Streamlit
- Biopython
- OpenAI API
- Git / GitHub

## 工夫した点

- `.env` によるAPIキー管理
- `.gitignore` による秘密情報保護
- 低コストモデル（GPT-4.1 nano）利用

## 今後の改善

- 患者向け要約モード
- 専門家向け要約モード
- 疾患名・薬剤名の自動抽出