import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')

def sentiment_analysis(input_text):
    analyzer = SentimentIntensityAnalyzer()

    scores = analyzer.polarity_scores(input_text)

    if scores['compound'] > 0.05:
        return "Positive"
    elif scores['compound'] < -0.05:
        return "Negative"
    else:
        return "Neutral"


input_text = input("Enter some text: ")
sentiment = sentiment_analysis(input_text)
print("Sentiment:", sentiment)
