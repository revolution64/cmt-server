from flask import Flask
from flask import jsonify
from flask import request

from nlp import process_text
from collections import Counter

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process():
    result = process_text(request.json["text"])
    return jsonify(result)

if __name__ == '__main__':
    app.run()    