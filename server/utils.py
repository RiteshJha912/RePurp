import re

def extract_video_id(url):
    """Extracts the video ID from various YouTube URL formats."""
    patterns = [
        r"v=([a-zA-Z0-9_-]{11})",  # Regular YouTube watch URLs
        r"youtu\.be/([a-zA-Z0-9_-]{11})",  # Shortened URLs
        r"embed/([a-zA-Z0-9_-]{11})",  # Embedded videos
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None
