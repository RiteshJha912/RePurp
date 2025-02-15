from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_utils import get_youtube_data

app = Flask(__name__)
CORS(app)

def split_into_tweets(text, max_length=280):
    """Splits text into tweet-sized chunks while maintaining sentence structure."""
    import re
    sentences = re.split(r'(?<=[.!?]) +', text)  # Split by sentence endings
    tweets, current_tweet = [], ""

    for sentence in sentences:
        if len(current_tweet) + len(sentence) <= max_length:
            current_tweet += " " + sentence
        else:
            tweets.append(current_tweet.strip())
            current_tweet = sentence

    if current_tweet:
        tweets.append(current_tweet.strip())

    return [f"{i+1}/{len(tweets)}: {tweet}" for i, tweet in enumerate(tweets)]

@app.route('/process', methods=['POST'])
def process_url():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    response_data = get_youtube_data(url)
    
    if "transcript" in response_data and response_data["transcript"] != "Transcript not available.":
        response_data["tweets"] = split_into_tweets(response_data["transcript"])

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
