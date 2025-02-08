from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

app = Flask(__name__)
CORS(app)

def extract_video_id(url):
    """Extracts video ID from a YouTube URL."""
    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

@app.route('/process', methods=['POST'])
def process_url():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    video_id = extract_video_id(url)
    if not video_id:
        return jsonify({"error": "Invalid YouTube URL"}), 400

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return jsonify({"error": f"Error fetching the URL: {str(e)}"}), 400

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract title
    title = soup.title.string if soup.title else 'No title found'

    # Extract description
    description = ''
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    if desc_tag and 'content' in desc_tag.attrs:
        description = desc_tag['content']
    else:
        # Check Open Graph description
        og_desc_tag = soup.find('meta', property='og:description')
        if og_desc_tag and 'content' in og_desc_tag.attrs:
            description = og_desc_tag['content']
        else:
            description = 'No description found'

    # Extract Open Graph image
    image = ''
    og_image_tag = soup.find('meta', property='og:image')
    if og_image_tag and 'content' in og_image_tag.attrs:
        image = og_image_tag['content']
    else:
        # Fallback to the first image in the page
        img_tag = soup.find('img')
        if img_tag and 'src' in img_tag.attrs:
            image = img_tag['src']
        else:
            image = 'No image found'

    # Fetch transcript
    transcript = ''
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([entry['text'] for entry in transcript_list])
    except (TranscriptsDisabled, NoTranscriptFound):
        transcript = 'Transcript not available for this video.'

    return jsonify({
        "title": title,
        "description": description,
        "image": image,
        "transcript": transcript
    })

if __name__ == '__main__':
    app.run(debug=True)
