import os
import googleapiclient.discovery
# This imports the discovery module from the googleapiclient library. This module allows us to discover and use APIs provided by Google.
from textblob import TextBlob
# This imports the TextBlob class from the textblob library. TextBlob is a Python library for processing textual data, including natural language processing tasks like sentiment analysis.

API_KEY = "Your youtube API Key"
# This line defines a variable API_KEY which stores your YouTube Data API key. This key is used to authenticate and authorize requests to the YouTube Data API.

def get_video_comments(video_id):# This is a function that takes a video_id as an argument. It is responsible for fetching comments from a YouTube video with the given video_id.
    api_service_name = "youtube"# This specifies the API service we want to use, which is the YouTube Data API.
    api_version = "v3"# This specifies the version of the YouTube Data API we want to use.
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)
#  This line creates a youtube object using the googleapiclient.discovery.build method. It builds a service object for interacting with the YouTube API using the specified parameters.

    # Request comments for the given video
    request = youtube.commentThreads().list(# This creates a list request to the commentThreads endpoint of the YouTube API.
        part="snippet",# This specifies that we want to retrieve the snippet part of the comments, which includes information like the comment text.
        videoId=video_id,# This specifies the ID of the YouTube video for which we want to retrieve comments.
        textFormat="plainText"#  This specifies that we want the comment text to be returned in plain text format.
    )
    response = request.execute()# This sends the request to the YouTube API and executes it, returning a response. The response contains the comments for the specified video.

# This part of the code processes the response from the YouTube API to extract the comments.>>>>
    comments = []
    for item in response["items"]:# It loops through each item in the response's "items" list.
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)
# <<<<For each item, it retrieves the comment text from item["snippet"]["topLevelComment"]["snippet"]["textDisplay"] and appends it to the comments list.
    return comments
# <<<<The get_video_comments function returns the list of comments extracted from the YouTube API response.

# Function to perform sentiment analysis
def analyze_sentiment(text):# This is a function that takes a text input (comment text) and performs sentiment analysis using TextBlob.
    blob = TextBlob(text)# This creates a TextBlob object from the input text.
    sentiment_score = blob.sentiment.polarity# This calculates the sentiment polarity score of the text. The polarity method of TextBlob returns a value between -1 and 1, where negative values indicate negative sentiment, positive values indicate positive sentiment, and 0 indicates neutral sentiment.
    if sentiment_score > 0.05:
        return "Positive"
    elif sentiment_score < -0.05:
        return "Negative"
    else:
        return "Neutral"
# <<<<The function then returns "Positive", "Negative", or "Neutral" based on the sentiment score.

if __name__ == "__main__":# This is a common Python idiom that allows the code block to be executed when the script is run directly (not imported as a module).
    video_id = "uwLWf0rEL18"  # Replace with the ID of the YouTube video. In the YT video link check the value v=" "; that is your video_id
    comments = get_video_comments(video_id)# This calls the get_video_comments function with the specified video_id to retrieve the comments for that video.

    print("Analyzing sentiment of comments...")

# The script then goes through each comment, performs sentiment analysis using analyze_sentiment, and prints out the comment along with its sentiment.>>>>
    for comment in comments:
        sentiment = analyze_sentiment(comment)
        print(f"Comment: {comment}")
        print(f"Sentiment: {sentiment}")
        print("=" * 20)
