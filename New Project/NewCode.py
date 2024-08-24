from flask import Flask, request, render_template, jsonify
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    texts = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return texts

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiments = [sentence.sentiment.polarity for sentence in blob.sentences]
    return sentiments

def plot_sentiments(sentiments):
    plt.figure(figsize=(10, 6))
    plt.plot(sentiments, marker='o', linestyle='-', color='b')
    plt.title('Sentiment Analysis')
    plt.xlabel('Sentence')
    plt.ylabel('Sentiment Polarity')
    plt.grid(True)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form['url']
    text = scrape_website(url)
    sentiments = analyze_sentiment(text)
    plot_url = plot_sentiments(sentiments)
    return jsonify({'plot_url': plot_url, 'sentiments': sentiments})

if __name__ == '__main__':
    app.run(debug=True)
