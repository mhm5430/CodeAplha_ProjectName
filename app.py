import streamlit as st
from deep_translator import MyMemoryTranslator
from gtts import gTTS
import io

# Page Configuration
st.set_page_config(page_title="AI Language Translator", page_icon="🌐", layout="centered")

st.title("🌐 AI Language Translation Tool")
st.write("Translate text instantly across multiple languages cleanly.")

# Supported Languages Mapping (MyMemory Language Codes)
languages = {
    'English': 'en-GB',
    'Urdu': 'ur-PK',
    'Spanish': 'es-ES',
    'French': 'fr-FR',
    'German': 'de-DE',
    'Arabic': 'ar-SA',
    'Chinese': 'zh-CN',
    'Hindi': 'hi-IN'
}

# Input UI
text_input = st.text_area("Enter Text to Translate:", height=150, placeholder="Type your text here...")

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language:", list(languages.keys()), index=0)
with col2:
    target_lang = st.selectbox("Target Language:", list(languages.keys()), index=1)

# Action Button
if st.button("Translate Text", type="primary"):
    if text_input.strip() != "":
        try:
            src_code = languages[source_lang]
            tgt_code = languages[target_lang]
            
            # Translation via MyMemory Engine
            translator = MyMemoryTranslator(source=src_code, target=tgt_code)
            translated_text = translator.translate(text_input)
            
            # Display Output
            st.success("### Translated Text:")
            st.write(f"**{translated_text}**")
            
            # Text-to-Speech (Audio player)
            tts_lang = tgt_code.split('-')[0] # Extract primary lang code for gTTS
            tts = gTTS(text=translated_text, lang=tts_lang)
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            st.audio(fp, format='audio/mp3')

        except Exception as e:
            st.error(f"Error during translation: {e}")
    else:
        st.warning("Please enter some text to translate.")
        