 Overview
This Python script retrieves comments from a YouTube video and performs sentiment analysis using the VADER sentiment analysis tool. It categorizes comments as positive, negative, or neutral and displays the overall sentiment along with the top 10 most positive and negative comments.

Requirements
requests
vaderSentiment
Install dependencies:pip install requests vaderSentiment

Usage
API Key: Replace API_KEY with your YouTube Data API key.

Video ID: Replace VIDEO_ID with the target YouTube video ID.

Run the script:python script_name.py
Output:
Final Sentiment Analysis Conclusion:
Overall Sentiment: Positive (Average Compound Score: 0.15)

Top 10 Most Positive Comments:
Author: User1, Score: 0.9
Comment: This is an amazing video!
--------------------------------------------------
...

Top 10 Most Negative Comments:
Author: User2, Score: -0.8
Comment: I didn't like this video at all.
--------------------------------------------------
...

Troubleshooting
Failed to retrieve comments: Check API key and permissions.
No comments found: Ensure the video has comments and the API call succeeds.
