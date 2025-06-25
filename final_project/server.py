from flask import Flask, jsonify, request
from EmotionDetection.emotion_detector import emotion_detector

app = Flask(__name__)

app.run(host='0.0.0.0', port=5000)

@app.route('/')
def home():
    return "<h1> You're good to go<h1>"

@app.route('/emotionDetector')
def get_emotion():
    build_list = ""
    query = request.args.get('text')
    emotion_analysis = emotion_detector(query)

# Sometimes the list was unordered so I did this to make sure dominent was on bottom
    for key, value in emotion_analysis.items():
        if key is not 'dominent_emotion':
            build_list += f"<li>{key} : {value} </li>" 

    return f"""
    <p>For the Given statement, the system response is:</p>
    <ul>
        {build_list}
        <li>The dominent emotion is {emotion_analysis['dominent_emotion']}</li>
    </ul>
    """