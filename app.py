
import streamlit as st
from chatbot import get_answer
from faq_data import faqs

# Page configuration
st.set_page_config(
    page_title="TechBot - FAQ Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #17152e);
    color: #ffffff;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    background: linear-gradient(120deg, #27204d, #171d3d);
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #494078;
    margin-bottom: 25px;
}

.hero h1 {
    color: #ffffff;
    font-size: 38px;
    margin-bottom: 8px;
}

.hero p {
    color: #c5c5e8;
    font-size: 16px;
}

.stat-card {
    background: #1c2340;
    border: 1px solid #343d62;
    padding: 18px;
    border-radius: 14px;
    text-align: center;
}

.stat-number {
    color: #a78bfa;
    font-size: 28px;
    font-weight: bold;
}

.stat-label {
    color: #c6c8df;
    font-size: 13px;
}

.user-message {
    background: #43358b;
    color: white;
    padding: 14px 18px;
    border-radius: 16px 16px 4px 16px;
    margin: 10px 0 10px auto;
    max-width: 80%;
    width: fit-content;
}

.bot-message {
    background: #202a48;
    color: #f0f0ff;
    padding: 14px 18px;
    border-radius: 16px 16px 16px 4px;
    border: 1px solid #394769;
    margin: 10px auto 10px 0;
    max-width: 85%;
    width: fit-content;
}

.small-note {
    color: #a6aac8;
    font-size: 12px;
}

section[data-testid="stSidebar"] {
    background: #11172c;
}

.stButton > button {
    border-radius: 10px;
    border: 1px solid #6554a5;
}

.stChatInput {
    border-color: #7560c8;
}
</style>
""", unsafe_allow_html=True)


# Session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 I'm TechBot, your AI & Technology FAQ Assistant. Ask me anything about AI, Python, Machine Learning, NLP, and more!"
        }
    ]

if "question_count" not in st.session_state:
    st.session_state.question_count = 0


# Sidebar
with st.sidebar:
    st.markdown("## 🤖 TechBot")
    st.caption("AI & Technology FAQ Assistant")

    st.divider()

    st.markdown("### 💡 What can I answer?")

    topics = [
        "Artificial Intelligence",
        "Python Programming",
        "Machine Learning",
        "Deep Learning",
        "Natural Language Processing",
        "ChatGPT",
        "Computer Vision",
        "Data Science"
    ]

    for topic in topics:
        st.markdown(f"• {topic}")

    st.divider()

    st.markdown("### 📊 Chat Statistics")
    st.metric("Questions Asked", st.session_state.question_count)
    st.metric("Available FAQs", len(faqs))

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Chat cleared! 👋 Ask me a new question."
            }
        ]
        st.session_state.question_count = 0
        st.rerun()

    st.markdown("---")
    st.caption("Built with Python, Streamlit & NLP")


# Main header
st.markdown("""
<div class="hero">
    <h1>🤖 TechBot</h1>
    <p>Your Smart AI & Technology FAQ Assistant</p>
    <p>Ask questions and get instant answers using NLP and smart similarity matching.</p>
</div>
""", unsafe_allow_html=True)


# Statistics
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{len(faqs)}+</div>
        <div class="stat-label">Knowledge Questions</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">NLP</div>
        <div class="stat-label">Text Processing</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">AI</div>
        <div class="stat-label">Smart Matching</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### 💬 Chat with TechBot")
st.caption("Type your question below or try one of the suggested questions.")


# Suggested questions
suggestions = [
    "What is Artificial Intelligence?",
    "What is Python?",
    "What is Machine Learning?",
    "What is ChatGPT?"
]

st.markdown("**✨ Try asking:**")

suggestion_cols = st.columns(4)

for index, suggestion in enumerate(suggestions):
    with suggestion_cols[index]:
        if st.button(
            suggestion,
            key=f"suggestion_{index}",
            use_container_width=True
        ):
            st.session_state.pending_question = suggestion


# Display conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Process pending suggested question
if "pending_question" in st.session_state:
    user_input = st.session_state.pop("pending_question")
else:
    user_input = st.chat_input("Ask TechBot anything about AI & Technology...")


# Handle user question
if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    st.session_state.question_count += 1

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("🤖 TechBot is thinking..."):

            answer, score = get_answer(user_input)

            st.markdown(answer)

            if score >= 0.20:
                st.caption(
                    f"🎯 Matching confidence: {score * 100:.1f}%"
                )
            else:
                st.caption("💡 Try asking a question about AI or technology.")

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()


# Footer
st.markdown("---")

st.markdown(
    "<p style='text-align:center; color:#999bb9;'>"
    "TechBot FAQ Assistant | Built with Python, Streamlit & NLP"
    "</p>",
    unsafe_allow_html=True
)
