from flask import Flask, request, jsonify
from better_profanity import profanity
from pydantic import BaseModel

app = Flask(__name__)

@app.route('/profane', methods=['POST'])
def profane():
    # Get the user's mood from the request parameters
    sentence = request.form.get('text')
    output = profanity.censor(sentence)
    return jsonify({'cleantext': output})


if __name__ == '__main__':
    app.run(debug=True)
