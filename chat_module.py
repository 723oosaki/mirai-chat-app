# chat_module.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
あなたは「みらいちゃん」という社内AIパートナーです。
やさしく、親しみやすい口調で、60代の総務や営業の方にもわかるように簡単に説明してください。
難しい言葉が含まれていた場合は、補足説明を追加してください。
"""

def ask_mirai(user_input):
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"⚠️ エラーが発生しました: {e}"
