from flask import Flask
from flask import render_template, request
from email import feedparser
import feedparser

app = Flask(__name__)

NEWS_CHANNEL = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'ndtv': 'http://feeds.feedburner.com/ndtvnews-top-stories',
    'rediff': 'http://www.rediff.com/rss/inrss.xml'
}


@app.route('/', methods=['GET', 'POST'])
def home():
    query = request.args.get('search')  # Enable GET method
    if not query or query.lower() not in NEWS_CHANNEL:
        channel = 'bbc'
    else:
        channel = query

    feed = feedparser.parse(NEWS_CHANNEL[channel])
    news = feed['entries']
    # print(feed)
    return render_template('news.html', articles=news)


if __name__ == '__main__':
    app.run(debug=True)
