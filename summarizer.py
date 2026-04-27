import os

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, AuthenticationError


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def summarize_article(title: str, abstract: str) -> str:
    """
    論文タイトルとAbstractを受け取り、日本語要約を返す関数。
    """

    if abstract.strip() == "":
        return "Abstractがないため、要約できません。"

    prompt = f"""
あなたは生命科学・医学論文を正確に要約する専門家です。
以下の論文タイトルとAbstractを読み、日本語で要約してください。

注意:
- Abstractに書かれている内容だけに基づいてください
- 推測で補わないでください

出力形式:
1. 研究背景
2. 研究目的
3. 方法
4. 主な結果
5. 意義

論文タイトル:
{title}

Abstract:
{abstract}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {
                    "role": "system",
                    "content": "あなたは生命科学論文を正確に日本語要約するアシスタントです。"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as error:
        return f"要約中にエラーが発生しました: {error}"