######YouTube Comment Sentiment Analysis

### Project Description:

This project performs sentiment analysis on YouTube video comments to identify negative comments using the YouTube Data API and the TextBlob library for Natural Language Processing (NLP).

The application retrieves comments from a specified YouTube video and processes the text to classify sentiment. It focuses on identifying and listing the comments with negative sentiment, which can be useful for content creators and administrators to understand feedback, detect potentially harmful or toxic comments, and monitor audience reception.

### Key Features:
- **YouTube Data API Integration**: Fetches up to 100 comments per page from a specific YouTube video using the YouTube API. Handles pagination to gather all available comments.
- **Sentiment Analysis**: Uses TextBlob, an NLP tool, to analyze the polarity of each comment. Comments with negative polarity are filtered and displayed.
- **Real-time Feedback**: Provides real-time results on negative comments, helping users monitor and evaluate the sentiment of their video’s comment section.

### Tech Stack:
- **Python**: The core language used for the application.
- **Google API Client**: Used to interact with YouTube's Data API to fetch video comments.
- **TextBlob**: A simple NLP library used to perform sentiment analysis.
- **YouTube Data API**: Provides access to video comments.

### How It Works:
1. **Input**: The YouTube video ID and an API key for the YouTube Data API.
2. **Comment Fetching**: The program requests and retrieves all comments from the video using the YouTube Data API.
3. **Sentiment Analysis**: Each comment is analyzed for sentiment polarity using TextBlob. Comments with a negative sentiment (polarity < 0) are filtered out.
4. **Output**: The program prints out all the negative comments identified from the sentiment analysis.

This project can be extended for further functionality, such as visualizing sentiment trends, analyzing different sentiment categories (positive, neutral, negative), or even automating the removal of toxic comments from YouTube videos.

### Example Use Case:
- **Content Moderation**: A content creator or a channel moderator can use this project to quickly identify negative or potentially harmful comments on their videos, allowing for quicker response or moderation actions.

###The front-end is basic because this was a machine learning project.

![Screenshot 2024-09-12 210408](https://github.com/user-attachments/assets/b2da178c-0948-43e5-a267-5d35775165e6)




![Screenshot 2024-09-12 210844](https://github.com/user-attachments/assets/c2f082d6-cd9a-45e7-ad8d-52b05398c7f9)
