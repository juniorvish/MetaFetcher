from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from utils import extract_metadata

app = Flask(__name__)

@app.route('/fetch_metadata', methods=['POST'])
def fetch_metadata():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        metadata = extract_metadata(soup)
        return jsonify(metadata), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()