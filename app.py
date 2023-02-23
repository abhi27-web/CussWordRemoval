from flask import Flask, request, jsonify
from better_profanity import profanity
from pydantic import BaseModel

app = Flask(__name__)

class InputData(BaseModel):
    text: str

@app.route('/profane', methods=['POST'])
def profane():
    # Extract the input data from the request body
    input_data = InputData.parse_raw(request.data)

    # Apply profanity filter to the input text
    output = profanity.censor(input_data.text)

    # Return the output as JSON
    return jsonify({'cleantext': output})

if __name__ == '__main__':
    app.run(debug=True)
