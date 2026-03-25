from textblob import TextBlob

text = input("Enter a sentence: ")

# correction
corrected = TextBlob(text).correct()

# sentiment
sentiment = TextBlob(text).sentiment

print("Corrected:", corrected)
print("Sentiment:", sentiment)
