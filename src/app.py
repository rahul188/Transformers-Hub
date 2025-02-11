from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import streamlit as st
from models import (
    summarization,
    sentiment_analysis,
    question_answering,
    ner,
    translation,
    text_generation,
    speech_to_text,
    image_captioning,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def main():
    st.title("Transformer Hub: NLP Applications")
    st.sidebar.title("Select an NLP Task")
    
    task = st.sidebar.selectbox(
        "Choose a task:",
        [
            "Text Summarization",
            "Sentiment Analysis",
            "Question Answering",
            "Named Entity Recognition",
            "Machine Translation",
            "Text Generation",
            "Speech-to-Text",
            "Image Captioning",
        ],
    )

    if task == "Text Summarization":
        text_input = st.text_area("Enter text to summarize:")
        if st.button("Summarize"):
            summary = summarization.summarize(text_input)
            st.write("Summary:", summary)

    elif task == "Sentiment Analysis":
        text_input = st.text_area("Enter text for sentiment analysis:")
        if st.button("Analyze"):
            sentiment = sentiment_analysis.analyze(text_input)
            st.write("Sentiment:", sentiment)

    elif task == "Question Answering":
        context = st.text_area("Enter context:")
        question = st.text_input("Enter your question:")
        if st.button("Get Answer"):
            answer = question_answering.answer(context, question)
            st.write("Answer:", answer)

    elif task == "Named Entity Recognition":
        text_input = st.text_area("Enter text for NER:")
        if st.button("Recognize Entities"):
            entities = ner.recognize_entities(text_input)
            st.write("Entities:", entities)

    elif task == "Machine Translation":
        text_input = st.text_area("Enter text to translate:")
        target_language = st.selectbox("Select target language:", ["es", "fr", "de"])
        if st.button("Translate"):
            translation_result = translation.translate(text_input, target_language)
            st.write("Translation:", translation_result)

    elif task == "Text Generation":
        prompt = st.text_area("Enter prompt for text generation:")
        if st.button("Generate Text"):
            generated_text = text_generation.generate(prompt)
            st.write("Generated Text:", generated_text)

    elif task == "Speech-to-Text":
        audio_file = st.file_uploader("Upload audio file:", type=["wav", "mp3"])
        if st.button("Convert to Text"):
            if audio_file is not None:
                text_output = speech_to_text.convert(audio_file)
                st.write("Transcribed Text:", text_output)

    elif task == "Image Captioning":
        image_file = st.file_uploader("Upload image file:", type=["jpg", "png"])
        if st.button("Generate Caption"):
            if image_file is not None:
                caption = image_captioning.caption(image_file)
                st.write("Caption:", caption)

if __name__ == "__main__":
    main()