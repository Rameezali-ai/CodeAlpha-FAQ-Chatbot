
# 🤖 TechBot - AI & Technology FAQ Chatbot

TechBot is an intelligent FAQ chatbot developed using Python, Streamlit, and Natural Language Processing (NLP).

It matches user questions with a knowledge dataset using TF-IDF vectorization and Cosine Similarity.

## ✨ Features

- Interactive chat interface
- 40+ frequently asked questions
- Multiple knowledge categories
- NLP text preprocessing using NLTK
- TF-IDF vectorization
- Cosine Similarity matching
- Similarity score display
- Unknown question handling
- Chat history
- Suggested questions
- Clear chat functionality
- Dark-themed user interface

## 🛠️ Technologies Used

- Python
- Streamlit
- NLTK
- Scikit-learn
- TF-IDF
- Cosine Similarity

## 📂 Project Structure

```text
CodeAlpha_FAQ_Chatbot/
│
├── app.py
├── chatbot.py
├── faq_data.py
├── requirements.txt
└── README.md
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rameezali-ai/CodeAlpha-FAQ-Chatbot.git
```

### 2. Open the project folder

```bash
cd CodeAlpha-FAQ-Chatbot
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

## 🧠 How It Works

1. User enters a question.
2. NLTK preprocesses the text.
3. TF-IDF converts questions into numerical vectors.
4. Cosine Similarity compares the user question with stored FAQs.
5. The chatbot returns the most relevant answer if the similarity score meets the threshold.

## 👨‍💻 Developer

**Rameez Ali**

GitHub: https://github.com/Rameezali-ai

## 📌 Internship Project

Developed as part of the CodeAlpha Artificial Intelligence Internship.
