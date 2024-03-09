import os
import googleapiclient.discovery
from textblob import TextBlob

# YouTube Data API Key
API_KEY = "AIzaSyD9UbMLnzgNsyfTODak1V0UtWaJlZsc6dE"

# Function to get comments from a YouTube video
def get_video_comments(video_id):
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    # Request comments for the given video
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText"
    )
    response = request.execute()

    comments = []
    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    return comments

# Function to perform sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    video_id = "uwLWf0rEL18"  # Replace with the ID of the YouTube video
    comments = get_video_comments(video_id)

    print("Analyzing sentiment of comments...")
    for comment in comments:
        sentiment = analyze_sentiment(comment)
        print(f"Comment: {comment}")
        print(f"Sentiment: {sentiment}")
        print("=" * 20)
