import streamlit as st
from models.summarization import generate_summary
from models.sentiment_analysis import analyze_sentiment
from models.question_answering import answer_question
from models.ner import perform_ner
from models.translation import translate_text
from models.text_generation import generate_text
from models.speech_to_text import convert_speech_to_text
from models.image_captioning import caption_image

st.title("Transformer Hub - NLP Applications")

st.sidebar.title("Select an NLP Task")
task = st.sidebar.selectbox("Choose a task", [
    "Text Summarization",
    "Sentiment Analysis",
    "Question Answering",
    "Named Entity Recognition (NER)",
    "Machine Translation",
    "Text Generation",
    "Speech-to-Text",
    "Image Captioning"
])

if task == "Text Summarization":
    st.subheader("Text Summarization")
    input_text = st.text_area("Enter text to summarize:")
    if st.button("Generate Summary"):
        if input_text:
            summary = generate_summary(input_text)
            st.write("Summary:")
            st.write(summary)
        else:
            st.error("Please enter some text.")

elif task == "Sentiment Analysis":
    st.subheader("Sentiment Analysis")
    input_text = st.text_area("Enter text for sentiment analysis:")
    if st.button("Analyze Sentiment"):
        if input_text:
            sentiment = analyze_sentiment(input_text)
            st.write("Sentiment:", sentiment)
        else:
            st.error("Please enter some text.")

elif task == "Question Answering":
    st.subheader("Question Answering")
    context = st.text_area("Enter context:")
    question = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        if context and question:
            answer = answer_question(context, question)
            st.write("Answer:", answer)
        else:
            st.error("Please provide both context and question.")

elif task == "Named Entity Recognition (NER)":
    st.subheader("Named Entity Recognition (NER)")
    input_text = st.text_area("Enter text for NER:")
    if st.button("Perform NER"):
        if input_text:
            entities = perform_ner(input_text)
            st.write("Entities:", entities)
        else:
            st.error("Please enter some text.")

elif task == "Machine Translation":
    st.subheader("Machine Translation")
    input_text = st.text_area("Enter text to translate:")
    target_language = st.selectbox("Select target language", ["fr", "es", "de", "it"])
    if st.button("Translate"):
        if input_text:
            translation = translate_text(input_text, target_language)
            st.write("Translation:", translation)
        else:
            st.error("Please enter some text.")

elif task == "Text Generation":
    st.subheader("Text Generation")
    prompt = st.text_area("Enter a prompt:")
    if st.button("Generate Text"):
        if prompt:
            generated_text = generate_text(prompt)
            st.write("Generated Text:", generated_text)
        else:
            st.error("Please enter a prompt.")

elif task == "Speech-to-Text":
    st.subheader("Speech-to-Text")
    audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])
    if st.button("Convert Speech to Text"):
        if audio_file is not None:
            text = convert_speech_to_text(audio_file)
            st.write("Transcribed Text:", text)
        else:
            st.error("Please upload an audio file.")

elif task == "Image Captioning":
    st.subheader("Image Captioning")
    image_file = st.file_uploader("Upload image file", type=["jpg", "jpeg", "png"])
    if st.button("Generate Caption"):
        if image_file is not None:
            caption = caption_image(image_file)
            st.write("Generated Caption:", caption)
        else:
            st.error("Please upload an image file.")