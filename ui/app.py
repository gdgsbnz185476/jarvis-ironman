from flask import Flask, jsonify
from core.memory import load

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(load())

app.run(port=5001, debug=True)
