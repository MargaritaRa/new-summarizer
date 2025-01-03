import openai
import os
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime
import requests
import json

load_dotenv()

news_api_key = os.environ.get("NEWS_API_KEY")

client = openai.OpenAI()
model = "gpt-3.5-turbo-16k"

def get_news(topic):
    url = (
        f"https://newsapi.org/v2/everything?q={topic}&apikey={news_api_key}&pageSize=5"
    )

    try:
        response = requests.get(url)
        if response.status_code == 200:
            # indent just makes things look better
            news = json.dumps(response.json(), indent=4)
            news_json = json.loads(news)

            data = news_json

            # Access all the fiels == loop through
            status = data["status"]
            total_results = data ["totalResults"]
            articles = data["articles"]
            final_news = []

            # Loop through the articles
            for article in articles:
                source_name = article["source"]["name"]
                author = article["author"]
                title = article["title"]
                description = article["description"]
                url = article["url"]
                content = article["content"]
                title_description = f"""
                    Title: {title},
                    Author: {author},
                    Source: {source_name},
                    Description: {description},
                    URL: {url}

                """
                final_news.append(title_description)

            return final_news
        else:
            return []

        
    except requests.exceptions.RequestException as e:
        print("Error occured duriong API Request", e)








def main():
    news = get_news("bitcoin")
    print(news[0])



if __name__ == "__main__":
    main()