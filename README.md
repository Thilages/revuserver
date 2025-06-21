# RevU Server

A Flask-based API server that provides YouTube video transcript functionality. This server acts as a backend service for fetching and processing YouTube video transcripts.

## Features

- Fetch YouTube video transcripts using video ID
- Supports English transcripts (en, en-US, en-GB)
- RESTful API endpoint integration
- CORS support for frontend integration
- Error handling and validation

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd RevU
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

To start the development server:
```bash
python main.py
```

The server will run on `http://localhost:5000` by default.

## API Endpoints

### GET Transcript

Endpoint: `POST /get-transcript`

Request Body:
```json
{
    "video_id": "YOUR_VIDEO_ID"
}
```

Response:
- Success:
```json
{
    "transcript": "The full transcript text..."
}
```

- Error:
```json
{
    "error": "Error message"
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Success
- 400: Bad Request (missing video ID)
- 404: Transcript not found or other errors

## Dependencies

The project uses the following main dependencies:
- Flask: Web framework
- flask-cors: Cross-origin resource sharing
- youtube-transcript-api: YouTube transcript API client

## Environment Variables

No environment variables are required for basic operation. However, you may want to configure:
- `CORS_ORIGINS`: Allowed origins for CORS
- `DEBUG`: Development mode

## Development

The server is set up with debug mode enabled by default. During development, any changes to the code will automatically reload the server.


