from flask import Flask
from flask import jsonify
from flask import request
from flask import send_from_directory

from flask_cors import CORS

from nlp import process_text
from collections import Counter

app = Flask(__name__, static_url_path='/static')
CORS(app)

@app.route('/', methods=['POST'])
def process():
    result = process_text(request.json["text"])
    return jsonify(result)


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
