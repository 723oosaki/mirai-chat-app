# main.py
import streamlit as st
from chat_module import ask_mirai
import json
import pandas as pd

st.set_page_config(page_title="社内AIパートナー みらいちゃん", layout="wide")

# サイドバー
menu = st.sidebar.radio("みらいちゃんメニュー", ["AIに質問する", "よくある質問", "AIツール比較", "自動化ツール紹介"])

st.title("🤖 社内AIパートナー みらいちゃん")

if menu == "AIに質問する":
    st.subheader("💬 みらいちゃんに質問してみよう")
    user_input = st.text_input("質問を入力してください", key="input")
    if st.button("送信", key="send_button") and user_input:
        with st.spinner("みらいちゃんが考え中..."):
            response = ask_mirai(user_input)
            st.markdown(response)

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
