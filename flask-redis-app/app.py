# app/app.py
from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)
redis_host = os.environ.get("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/set', methods=['POST'])
def set_value():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    r.set(key, value)
    return jsonify({"message": "Key set"})

@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    value = r.get(key)
    return jsonify({key: value})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask
app = Flask(__name__)

@app.route('/health')
def health():
    return "OK", 200

