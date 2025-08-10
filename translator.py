import streamlit as st
from deep_translator import GoogleTranslator

# Title
st.title("Tweet Translator Tool")

# Language options
languages = {
    'English': 'en',
    'Hindi': 'hi',
    'Malayalam': 'ml',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de'
}

# Input tweet text
tweet_text = st.text_area("Enter the tweet text to translate:")

# Language selection
src_lang = st.selectbox("Source Language", list(languages.keys()))
target_lang = st.selectbox("Target Language", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if tweet_text.strip() == "":
        st.warning("Please enter a tweet.")
    else:
        translated = GoogleTranslator(
            source=languages[src_lang],
            target=languages[target_lang]
        ).translate(tweet_text)

        st.success("Translated Tweet:")
        st.write(translated)
