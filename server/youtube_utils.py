import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from utils import extract_video_id

def get_youtube_data(url):
    """Fetches metadata and transcript from a YouTube URL."""
    video_id = extract_video_id(url)
    if not video_id:
        return {"error": "Invalid YouTube URL"}

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": f"Error fetching the URL: {str(e)}"}

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract title
    title = soup.title.string if soup.title else 'No title found'

    # Extract description
    description = 'No description found'
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    if desc_tag and 'content' in desc_tag.attrs:
        description = desc_tag['content']
    else:
        og_desc_tag = soup.find('meta', property='og:description')
        if og_desc_tag and 'content' in og_desc_tag.attrs:
            description = og_desc_tag['content']

    # Extract thumbnail
    image = 'No image found'
    og_image_tag = soup.find('meta', property='og:image')
    if og_image_tag and 'content' in og_image_tag.attrs:
        image = og_image_tag['content']

    # Fetch transcript
    transcript = 'Transcript not available.'
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([entry['text'] for entry in transcript_list])
    except (TranscriptsDisabled, NoTranscriptFound):
        pass

    return {
        "title": title,
        "description": description,
        "image": image,
        "transcript": transcript
    }
