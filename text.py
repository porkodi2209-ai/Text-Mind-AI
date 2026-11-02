
import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Text Mind AI",
    page_icon="🤖",
    layout="wide"
)

st.title("Text Mind AI")
st.subheader("Hugging Face Pipeline Demonstration")

st.write(
    "An interactive application to explore "
    "Natural Language Processing using Hugging Face."
)

task = st.selectbox(
    "Select NLP Task",
    [
        "Summarization",
        "Translation",
        "Sentiment Analysis",
        "Question Answering"
    ]
)


@st.cache_resource
def load_flan():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-small"
    )


@st.cache_resource
def load_sentiment():
    return pipeline(
        "sentiment-analysis",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )


@st.cache_resource
def load_qa():
    return pipeline(
        "question-answering",
        model="deepset/tinyroberta-squad2"
    )


if task == "Summarization":

    st.header("Text Summarization")
    st.write("Convert long paragraphs into short summaries.")

    text = st.text_area(
        "Enter a long paragraph",
        height=200,
        placeholder="Enter text to summarize..."
    )

    if st.button("Summarize Text"):
        if text.strip():
            try:
                with st.spinner("Generating summary..."):
                    model = load_flan()

                    result = model(
                        "Summarize this text in simple English: " + text,
                        max_new_tokens=100,
                        do_sample=False
                    )

                st.success("Summary Generated Successfully!")
                st.write(result[0]["generated_text"])

            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter some text.")


elif task == "Translation":

    st.header("Language Translation")
    st.write("Translate text into your preferred language.")

    text = st.text_area(
        "Enter Your Text",
        height=150,
        placeholder="Enter the text you want to translate..."
    )

    language = st.text_input(
        "Enter Target Language",
        placeholder="Example: Tamil, Hindi, French, German..."
    )

    if st.button("Translate Text"):
        if text.strip() and language.strip():
            try:
                with st.spinner("Translating..."):
                    model = load_flan()

                    result = model(
                        f"Translate the following text into {language}: {text}",
                        max_new_tokens=200,
                        do_sample=False
                    )

                st.success("Translation Completed!")
                st.subheader(f"Translated Text ({language})")
                st.write(result[0]["generated_text"])

            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter text and target language.")


elif task == "Sentiment Analysis":

    st.header("Sentiment Analysis")
    st.write("Identify the emotional tone of a given text.")

    text = st.text_area(
        "Enter a sentence",
        placeholder="Example: I really love this application!"
    )

    if st.button("Analyze Sentiment"):
        if text.strip():
            try:
                with st.spinner("Analyzing sentiment..."):
                    sentiment = load_sentiment()
                    result = sentiment(text)

                label = result[0]["label"]
                score = result[0]["score"]

                st.success("Analysis Completed!")
                st.write("Sentiment:", label)
                st.write("Confidence Score:", round(score, 4))

            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter some text.")


elif task == "Question Answering":

    st.header("Question Answering")
    st.write("Find answers from the given context.")

    context = st.text_area(
        "Enter Context",
        height=180,
        placeholder="Enter a paragraph containing the answer..."
    )

    question = st.text_input(
        "Enter Your Question",
        placeholder="Ask a question about the context..."
    )

    if st.button("Get Answer"):
        if context.strip() and question.strip():
            try:
                with st.spinner("Finding the answer..."):
                    qa = load_qa()

                    result = qa(
                        question=question,
                        context=context
                    )

                st.success("Answer Found!")
                st.write("Answer:", result["answer"])

                st.write(
                    "Confidence Score:",
                    round(result["score"], 4)
                )

            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter both context and question.")


st.divider()

st.caption(
    "Text Mind AI | Developed using Python, Streamlit and Hugging Face Transformers."
)
