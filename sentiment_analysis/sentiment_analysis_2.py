import nltk.data
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment_Analysis(message_text):
        sid = SentimentIntensityAnalyzer()
        tokenizer = nltk.data.load('saved_model/english.pickle')
        sentences = tokenizer.tokenize(message_text)
        emotion = dict()
        for sentence in sentences:
                scores = sid.polarity_scores(sentence)
                for key in sorted(scores):
                        emotion[key] = scores[key]
        emotion_value = emotion.get('compound')
        if emotion_value > 0:
                if emotion_value > 0.9:
                        return "Very happy"
                elif emotion_value > 0.7:
                        return "Enthusiastic"
                elif emotion_value > 0.5:
                        return "Happy"
                elif emotion_value > 0.2:
                        return "Neutral"
                else:
                        return "Completely Neutral"

        else:
                if emotion_value < -0.9:
                        return "Abusive"
                elif emotion_value < -0.7:
                        return "Angry"
                elif emotion_value < -0.5:
                        return "Very sad"
                elif emotion_value < -0.2:
                        return "Sad"
                else:
                        return "Negative feelings"





