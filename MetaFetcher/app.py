from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/fetch_metadata', methods=['POST'])
def fetch_metadata():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    metadata = utils.get_metadata(url)
    if metadata:
        return jsonify(metadata), 200
    else:
        return jsonify({"error": "Failed to fetch metadata"}), 500

if __name__ == '__main__':
    app.run()