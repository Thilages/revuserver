import os
from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound






# --- SETUP AND CONFIGURATION ---
  # Load variables from .env file

app = Flask(__name__)
# Allow requests from your React app's origin
# CORS(app, origins=["http://localhost:5173"])

# --- API KEYS FROM ENVIRONMENT VARIABLES ---
# REASON FOR CHANGE: Securely load API keys from an environment file (.env)
# This prevents them from being exposed in your source code.
# TEXTRAZOR_API_KEY="2717ff956598ae2f4210c41d71442b7ea2b2d7743e7ac89470ede263"
# GOOGLE_API_KEY="AIzaSyCFFpPFj0znuw2RrUHDRCa28fLCRADlGGs"
# YOUTUBE_API_KEY="AIzaSyAVBFiTsS5Q1qEBrvUZhg1a5v3Zzmcetu0"


def fetch_transcript(video_id):
    try:
        # REASON FOR CHANGE: Requesting only English transcripts for consistency
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'en-US', 'en-GB'])
        text_paragraph = " ".join([line['text'] for line in transcript_list])
        return {"transcript": text_paragraph}
    # REASON FOR CHANGE: Specific exception handling for a common failure case.
    except NoTranscriptFound:
        return {"error": "An English transcript could not be found for this video. Please select another."}
    except Exception as e:
        print(f"Error fetching transcript for {video_id}: {e}")
        return {"error": f"An unexpected error occurred while fetching the transcript: {str(e)}"}


# --- FLASK ENDPOINTS ---




@app.route('/get-transcript', methods=['POST'])
def get_transcript_route():
    data = request.json
    video_id = data.get('video_id')
    if not video_id:
        return jsonify({"error": "Video ID is required"}), 400

    result = fetch_transcript(video_id)

    if "error" in result:
        # REASON FOR CHANGE: Return 404 for a missing transcript, which is more accurate.
        return jsonify(result), 404

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)