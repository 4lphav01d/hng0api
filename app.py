from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def get_info():
    
    response = {
        "email": "daniel.chukwu@miva.edu.ng",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/4lphav01d/hng-api"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
    