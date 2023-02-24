from flask import Flask, request, jsonify
from better_profanity import profanity
from pydantic import BaseModel

app = Flask(__name__)

@app.route('/profane/<text>', methods=['GET'])
def profane(text):
    output = profanity.censor(text)
    return jsonify({'cleantext': output})


if __name__ == '__main__':
    app.run(debug=True)
