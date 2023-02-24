from flask import Flask, request, jsonify
from better_profanity import profanity
from pydantic import BaseModel

app = Flask(__name__)

@app.route('/profane/<input_string>')
def convert_to_profane(input_string):
    # Convert input string to profane version
    output = profanity.censor(input_string.replace(" ", "_"))

    # Return the profane string as a response
    return jsonify({'cleantext': output.replace("_", " ")})

if __name__ == '__main__':
    app.run()
