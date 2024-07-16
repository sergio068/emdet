from flask import Flask, request, jsonify
from my_emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    emotions, status = emotion_predictor(text)
    if status == 500:
        return jsonify(emotions), 500
    return jsonify(emotions)

if __name__ == '__main__':
    app.run(debug=True)

