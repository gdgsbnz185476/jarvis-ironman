from flask import Flask, request, jsonify
from core.agent import run_agent

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    message = data["message"]

    response = run_agent(message)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5005, debug=True)
