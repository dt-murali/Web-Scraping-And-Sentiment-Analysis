import nltk
nltk.download('vader_lexicon')

from flask import Flask, request, render_template, send_from_directory
from scraper import AmazonScraper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        scraper = AmazonScraper(url)

        if scraper:
            reviews = scraper.get_reviews()
            scraper.plot_sentiment_analysis(reviews)
            return render_template('index.html', reviews=reviews)
    
    return render_template('index.html', reviews=None)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)

