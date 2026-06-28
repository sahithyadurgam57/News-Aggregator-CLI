import streamlit as st
import requests
import pandas as pd

API_KEY = "d8d1069fa27047aca9682b83441d2883"

st.title("News Aggregator")

topic = st.text_input("Enter News Topic")

if st.button("Get News"):

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data["status"] == "ok":

        news = []

        for article in data["articles"]:
            news.append({
                "Title": article["title"],
                "Source": article["source"]["name"]
            })

        df = pd.DataFrame(news)

        st.dataframe(df)

    else:
        st.error("Failed to fetch news")