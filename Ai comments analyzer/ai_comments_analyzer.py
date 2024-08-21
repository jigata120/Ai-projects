import requests
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

API_KEY = "AIzaSyBTfNGhbrL5YPBN7Jj8wjfgAtbwmcoTzFM"
VIDEO_ID = "q5-1qpYcdrM"
MAX_RESULTS = 50

analyzer = SentimentIntensityAnalyzer()

positive_comments = []
negative_comments = []
compound_scores = []

url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={VIDEO_ID}&maxResults={MAX_RESULTS}&key={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    comments_data = response.json()

    for item in comments_data.get("items", []):
        comment = item["snippet"]["topLevelComment"]["snippet"]
        author = comment["authorDisplayName"]
        text = comment["textDisplay"]

        sentiment = analyzer.polarity_scores(text)
        compound_score = sentiment["compound"]
        compound_scores.append(compound_score)

        if compound_score >= 0.05:
            positive_comments.append((compound_score, author, text))
        elif compound_score <= -0.05:
            negative_comments.append((compound_score, author, text))

    if compound_scores:
        average_compound = sum(compound_scores) / len(compound_scores)

        print("\nFinal Sentiment Analysis Conclusion:")
        if average_compound >= 0.05:
            print(
                f"Overall Sentiment: Positive (Average Compound Score: {average_compound:.2f})"
            )
        elif average_compound <= -0.05:
            print(
                f"Overall Sentiment: Negative (Average Compound Score: {average_compound:.2f})"
            )
        else:
            print(
                f"Overall Sentiment: Neutral (Average Compound Score: {average_compound:.2f})"
            )
    else:
        print("No comments found to analyze.")

    positive_comments.sort(reverse=True, key=lambda x: x[0])
    negative_comments.sort(key=lambda x: x[0])

    top_positive_comments = positive_comments[:10]
    top_negative_comments = negative_comments[:10]

    print("\nTop 10 Most Positive Comments:")
    for score, author, text in top_positive_comments:
        print(f"Author: {author}, Score: {score}")
        print(f"Comment: {text}")
        print("-" * 50)

    print("\nTop 10 Most Negative Comments:")
    for score, author, text in top_negative_comments:
        print(f"Author: {author}, Score: {score}")
        print(f"Comment: {text}")
        print("-" * 50)
else:
    print(f"Failed to retrieve comments: {response.status_code}")
    print(response.text)
