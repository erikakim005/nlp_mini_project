import streamlit as st   # st= nickname / streamlit = library that build web apps only using python
from textblob import TextBlob # instead of importing the whole texblob library, u just import the TextBlob class form it 
# TextBlob = NLP tool that handles things like spell correction and sentimenr analysis

st.title("✨ NLP Mini App") # display title in streamlit site 

st.write("Type a sentence and click Analyze 👇") # st.write() = most basic way to display text on screen

text = st.text_input("Enter a sentence:") # create text input box on the screen 

analyze = st.button("Analyze") # when clicked = True / not clicked = False

if analyze and text: # = the code will only run when the text is not empty!
    blob = TextBlob(text) # variable blob will store the input text into a TextBlob object

    #correction
    corrected = str(blob.correct()) # str(blob.correct()) = TexBlob fix spelling and convert it to string. and sotre in variable corrected
    
    #sentiment
    polarity = blob.sentiment.polarity # sentiment= contain emotional info / polarity = pulls out just the positive or negative score 
    
    if polarity > 0: 
        sentiment_label = "Positive 😊"
    elif polarity < 0:
        sentiment_label = "Negative 😢"
    else:
        sentiment_label = "Neutral 😐"

    # UI
    st.subheader("Corrected Sentence") # st.subheader() = mediu sized heading 
    st.success(corrected) # success message = text inside GREEN box 

    st.subheader("Sentiment")
    st.info(sentiment_label) # info mnassages = tect inside BLUE bow
