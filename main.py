# main.py
import streamlit as st
from chat_module import ask_mirai
import json
import pandas as pd

st.set_page_config(page_title="社内AIパートナー みらいちゃん", layout="wide")

# セッションで会話履歴を保持
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# サイドバー
menu = st.sidebar.radio("みらいちゃんメニュー", ["AIに質問する", "よくある質問", "AIツール比較", "自動化ツール紹介", "初めての方へ"])

st.title("🤖 社内AIパートナー みらいちゃん")

if menu == "AIに質問する":
    st.subheader("💬 みらいちゃんに質問してみよう")
    with st.form(key="chat_form"):
        col1, col2 = st.columns([5, 1])
        user_input = col1.text_input("", placeholder="質問を入力してください", label_visibility="collapsed", key="input")
        send = col2.form_submit_button("🚀 送信")

        if send and user_input:
            with st.spinner("みらいちゃんが考え中..."):
                response = ask_mirai(user_input, st.session_state.chat_history)
                st.session_state.chat_history.append({"role": "user", "content": user_input})
                st.session_state.chat_history.append({"role": "assistant", "content": response})

    # 会話履歴表示
    for message in st.session_state.chat_history:
        st.chat_message(message["role"]).markdown(message["content"])

elif menu == "よくある質問":
    st.subheader("📚 よくある質問")
    with open("data/faq.json", "r", encoding="utf-8") as f:
        faqs = json.load(f)
    for item in faqs:
        with st.expander(f"Q: {item['question']}"):
            st.markdown(f"A: {item['answer']}")

elif menu == "AIツール比較":
    st.subheader("📊 AIツールの比較")
    df = pd.read_csv("data/tool_comparison.csv")
    st.dataframe(df, use_container_width=True)

elif menu == "自動化ツール紹介":
    st.subheader("🔧 自動化ツールの紹介")
    df = pd.read_csv("data/automation_tools.csv")
    for _, row in df.iterrows():
        st.markdown(f"### 🔹 {row['ツール名']}")
        st.markdown(f"**概要：** {row['概要']}")
        st.markdown(f"**主な使い方：** {row['使い方']}")
        st.markdown("---")

elif menu == "初めての方へ":
    st.subheader("👋 初めての方へ")
    st.markdown("""
        このアプリ「みらいちゃん」は、社内でAIを使いこなしたい方向けのサポートパートナーです。

        ### 💡できること：
        - ChatGPT（生成AI）に自然な言葉で質問ができる
        - よくある質問をワンクリックで見られる
        - どのAIツールがいいのか分かるツール比較
        - 業務を楽にする自動化ツールの紹介
        - むずかしい言葉もやさしく解説（用語集）

        **はじめてでも大丈夫です！左のメニューから使いたい機能を選んでください。**
    """)
