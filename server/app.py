from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_utils import get_youtube_data

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_url():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    response_data = get_youtube_data(url)
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
