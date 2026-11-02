# Text Mind AI

## Project Description
Text Mind AI is a simple Natural Language Processing application developed using Python, Streamlit, and Hugging Face Transformers. It performs different text-related tasks using pre-trained language models.

## Features

1. **Text Summarization** – Converts long paragraphs into short summaries.
2. **Text Translation** – Translates text into a user-specified target language.
3. **Sentiment Analysis** – Identifies whether the given text expresses positive or negative sentiment.
4. **Question Answering** – Provides answers based on the given context and question.

## Technologies Used
- Python
- Streamlit
- Hugging Face Transformers
- PyTorch

## Models Used
- Summarization: `google/flan-t5-small`
- Translation: `google/flan-t5-small`
- Sentiment Analysis: `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
- Question Answering: `deepset/tinyroberta-squad2`

## Installation

### 1. Clone the Repository
```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Navigate to the Project Folder
```bash
cd "LLM Week 7"
```

### 3. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run text.py
```

## Demo
## Screenshot

<img width="1920" height="1080" alt="Screenshot (173)" src="https://github.com/user-attachments/assets/d34e4d02-01d3-45b6-9ca5-760a1e69525d" />

<img width="1920" height="1080" alt="Screenshot (174)" src="https://github.com/user-attachments/assets/38c0bb20-6fda-4f25-ba4d-e52736a6d049" />

<img width="1920" height="1080" alt="Screenshot (175)" src="https://github.com/user-attachments/assets/ddf418de-a37a-4e7d-bd5f-b6af6b57c7aa" />

<img width="1920" height="1080" alt="Screenshot (176)" src="https://github.com/user-attachments/assets/17ad4288-0268-4a43-9c3b-72592f95c80c" />

<img width="1920" height="1080" alt="Screenshot (177)" src="https://github.com/user-attachments/assets/de58b7fd-d604-4b0e-9efe-031aa88637b9" />

<img width="1920" height="1080" alt="Screenshot (178)" src="https://github.com/user-attachments/assets/f2634b52-4ff8-49a7-9435-a17871a55845" />

<img width="1920" height="1080" alt="Screenshot (179)" src="https://github.com/user-attachments/assets/f9868301-9d10-4a0b-8191-f32c33f818f0" />

<img width="1920" height="1080" alt="Screenshot (180)" src="https://github.com/user-attachments/assets/079c1cfe-db0d-4e8c-84ab-b7299d08a4c5" />


## Project Structure
```text
LLM Week 7/
│
├── text.py
├── requirements.txt
└── README.md
```

## Learning Outcomes
- Understanding Hugging Face Pipelines.
- Implementing NLP tasks using pre-trained models.
- Working with text summarization and translation.
- Performing sentiment analysis.
- Building question-answering applications.
- Developing interactive applications using Streamlit.
