from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

app = Flask(__name__)
CORS(app, origins=["https://revu-eight.vercel.app"])  # Replace with your Vercel app's URL

def fetch_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'en-US', 'en-GB'])
        text_paragraph = " ".join([line['text'] for line in transcript_list])
        return {"transcript": text_paragraph}
    except NoTranscriptFound:
        return {"error": "An English transcript could not be found for this video. Please select another."}
    except Exception as e:
        print(f"Error fetching transcript for {video_id}: {e}")
        return {"error": f"An unexpected error occurred while fetching the transcript: {str(e)}"}

@app.route('/get-transcript', methods=['POST'])
def get_transcript_route():
    data = request.json
    video_id = data.get('video_id')
    if not video_id:
        return jsonify({"error": "Video ID is required"}), 400

    result = fetch_transcript(video_id)

    if "error" in result:
        return jsonify(result), 404

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
