import streamlit as st
from googletrans import Translator
st.title("language translator app")
input=st.text_area("Enter text into translate")

target=st.selectbox("Select Target Language", ["ar", "hi", "sd", "pa", "ur"])

if st.button("Translate"):
    translator = Translator()
    translation = translator.translate(input, dest=target)
    st.success(f"Translated Text: {translation.text}")