```
repurp/
├── README.md
├── .gitignore
├── client/                   # React frontend
│   ├── package.json
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   └── src/
│       ├── App.js            # Main App component
│       ├── index.js          # Entry point for React
│       ├── components/
│       │   └── FileUpload.js # Component for uploading videos
│       ├── styles/
│       │   └── App.css       # Global styles (if needed)
│       └── utils/
│           └── api.js        # Helper file for API calls (Axios/fetch wrappers)
└── server/                   # Flask backend
    ├── app.py                # Main Flask application file (API endpoints)
    ├── requirements.txt      # Python dependencies (Flask, etc.)
    ├── config.py             # Configuration variables (if needed)
    ├── uploads/              # Directory where uploaded videos and generated files are stored
    │   ├── audio/            # (Optional) Separated directory for extracted audio files
    │   ├── clips/            # (Optional) Separated directory for generated TikTok clips
    │   └── transcripts/      # (Optional) Separated directory for transcription files
    ├── static/               # (Optional) Static files served by Flask (if needed)
    │   └── clips/            # You can move the clips here for serving via URLs
    ├── whisper/              # (Optional) Directory for the whisper.cpp executable and related scripts/configs
    └── utils/                # Helper scripts for processing
        ├── video_processing.py  # Wrappers for FFmpeg commands (audio extraction, clipping)
        └── text_processing.py   # Functions for summarizing and extracting key points
```