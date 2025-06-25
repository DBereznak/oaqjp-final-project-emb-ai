from emotion_detector import emotion_detector

test_strings = ["I am glad this happened", "I am really mad about this", "I feel disgusted just hearing about this", "I am so sad about this", "I am really afraid that this will happen"]

for text in test_strings:
    emotion_detector(text)
