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
└── server/
    ├── .env                  # Environment variables (gitignored)
    ├── config/               # Split configs for dev/prod environments
    │   ├── __init__.py
    │   ├── development.py
    │   └── production.py
    ├── services/             # Renamed from "utils"
    │   ├── video_processor.py  # FFmpeg logic
    │   ├── content_generator.py  # AI post generation
    │   └── whisper_service.py  # Wrapper for whisper.cpp
    ├── tasks/                # (Optional) Background tasks (Celery)
    ├── models/               # (Optional) Database models if adding user auth later
    └── scripts/              # Maintenance scripts (e.g., clean_uploads.py)
```