import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translator App")
st.write("This app translates text into different languages using Google Translator.")

# Input text and language selection
text = st.text_area("Enter text to translate:", height=200)
target_lang = st.selectbox(
    "Select target language:",
    ["fr", "es", "de", "it", "pt", "ru", "zh-CN", "hi", "kn"],  # 'kn' is the correct code for Kannada
    format_func=lambda x: {
        "fr": "French",
        "es": "Spanish",
        "de": "German",
        "it": "Italian",
        "pt": "Portuguese",
        "ru": "Russian",
        "zh-CN": "Chinese (Simplified)",
        "hi": "Hindi",
        "kn": "Kannada"
    }.get(x, x)
)

# Translation function
def translate_text(text, target_lang):
    try:
        translated = GoogleTranslator(target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Error: {str(e)}"

# Translate button
if st.button("Translate"):
    if not text.strip():
        st.warning("⚠️ Please enter some text to translate.")
    else:
        translated_text = translate_text(text, target_lang)
        st.success("✅ Translated text:")
        st.write(translated_text)
