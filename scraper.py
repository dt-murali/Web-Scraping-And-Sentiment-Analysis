import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class BaseScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.sia = SentimentIntensityAnalyzer()

    def get_html(self, url):
        product_url = url
        rev_url = product_url.replace("dp", "product-reviews")
        response = requests.get(rev_url, headers=self.headers)
        response.raise_for_status()
        return response.content

    def parse_reviews(self, html_content):
        raise NotImplementedError("This method should be implemented by subclasses")

    def analyze_sentiment(self, text):
        score = self.sia.polarity_scores(text)
        return score

    def get_reviews(self):
        html_content = self.get_html(self.url)
        reviews = self.parse_reviews(html_content)
        for review in reviews:
            review['sentiment'] = self.analyze_sentiment(review['text'])
        return reviews

class AmazonScraper(BaseScraper):
    def parse_reviews(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        reviews = []

        review_elements = soup.find_all('div', {'data-hook': 'review'})
        for element in review_elements:
            review = {}
            rating_element = element.find('i', {'data-hook': 'review-star-rating'})
            if rating_element:
                review['rating'] = rating_element.text.strip().split(' ')[0]
            review_text_element = element.find('span', {'data-hook': 'review-body'})
            if review_text_element:
                review['text'] = review_text_element.text.strip()
            reviews.append(review)
        return reviews

    def plot_sentiment_analysis(self, reviews_df):
        if(reviews_df):
            rev_df = pd.DataFrame(reviews_df)
            rev_df.columns = ['rating', 'text', 'sentiment']
            comp_lst = ['Positive' if comp['compound'] > 0 else 'Negative' if comp['compound'] < 0 else 'Neutral' for comp in rev_df.sentiment]
            comp_lst_df = pd.DataFrame(comp_lst, columns=['sentiment'])

            os.makedirs('static', exist_ok=True)
        
            plt.figure(figsize=(10, 6))
            sns.countplot(x='sentiment', data=comp_lst_df, palette='viridis', hue='sentiment')
            plt.title('Sentiment Analysis of Amazon Product Reviews')
            plt.xlabel('Sentiment')
            plt.ylabel('Number of Reviews')
        
            plot_path = os.path.join('static', 'countplot.png')
            plt.savefig(plot_path)
            plt.close()
