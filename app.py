from flask import Flask, render_template, request
import pandas as pd
from textblob import TextBlob
from googleapiclient.discovery import build

app = Flask(__name__)

# Function to get sentiment
def get_sentiment(comment):
    analysis = TextBlob(comment)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Function to fetch comments from YouTube
def get_video_comments(video_id):
    # Replace 'YOUR_API_KEY' with your actual YouTube API key
    youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')
    comments = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100
    )
    while request:
        response = request.execute()
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        request = youtube.commentThreads().list_next(request, response)
    return comments

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_link = request.form['video_link']
        # Extract video ID from the link
        video_id = video_link.split('v=')[-1]
        # Fetch comments from YouTube
        comments = get_video_comments(video_id)
        # Perform sentiment analysis
        df = pd.DataFrame(comments, columns=['Comment'])
        df['Sentiment'] = df['Comment'].apply(get_sentiment)
        sentiment_counts = df['Sentiment'].value_counts().to_dict()
        return render_template('result.html', sentiment_counts=sentiment_counts)
    return render_template('sentiment.html')

