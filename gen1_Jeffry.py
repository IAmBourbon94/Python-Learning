def sentiment_analysis(input_text):

    positive_words = ["good", "happy", "excellent", "great", "awesome", "wonderful", "fantastic", "amazing", "superb", "joyful"]
    negative_words = ["bad", "sad", "terrible", "horrible", "awful", "miserable", "unhappy", "disappointing", "poor", "grim"]
 
    words = input_text.lower().split()

    
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"


input_text = input("Enter some text: ")
sentiment = sentiment_analysis(input_text)
print("Sentiment:", sentiment)
