
import re
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import faqs

stemmer = PorterStemmer()


# Text preprocessing
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    tokens = wordpunct_tokenize(text)

    words = [
        stemmer.stem(word)
        for word in tokens
        if word.strip()
    ]

    return " ".join(words)


# Prepare training dataset
questions = [faq["question"] for faq in faqs]

processed_questions = [
    preprocess_text(question)
    for question in questions
]


# Train TF-IDF model on FAQ dataset
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    stop_words="english"
)

faq_vectors = vectorizer.fit_transform(
    processed_questions
)


# Answer prediction
def get_answer(user_question):

    if not user_question.strip():
        return "Please enter a question.", 0.0

    processed_question = preprocess_text(user_question)

    user_vector = vectorizer.transform(
        [processed_question]
    )

    similarities = cosine_similarity(
        user_vector,
        faq_vectors
    )[0]

    best_index = similarities.argmax()
    best_score = similarities[best_index]

    if best_score < 0.25:
        return (
            "Sorry, I don't have enough information "
            "to answer this question. Please try another topic.",
            float(best_score)
        )

    answer = faqs[best_index]["answer"]

    return answer, float(best_score)
