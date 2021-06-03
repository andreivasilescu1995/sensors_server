#!usr/bin/env python3

from flask import Flask, request, jsonify
import json
from database import Database

app = Flask(__name__)

@app.route('/insert', methods=['POST', 'GET'])
def login():
    values = json.loads(request.data)['values']
    print(values)
    # db = Database()
    # db.insert(values)
    return jsonify('')

if __name__ == "__main__":
    app.run(debug=True)
