import streamlit as st
import json
import re

# Load knowledge base from JSON files
def load_knowledge_base():
    with open('knowledge_base_en.json', 'r', encoding='utf-8') as f:
        kb_en = json.load(f)
    with open('knowledge_base_fr.json', 'r', encoding='utf-8') as f:
        kb_fr = json.load(f)
    with open('knowledge_base_ar.json', 'r', encoding='utf-8') as f:
        kb_ar = json.load(f)
    return kb_en, kb_fr, kb_ar

# Function to find the best matching response
def get_best_response(question, knowledge_base):
    best_match = None
    highest_score = 0
    
    question = question.lower()
    for qa_pair in knowledge_base:
        score = sum(1 for word in question.split() if word in qa_pair['question'].lower())
        if score > highest_score:
            highest_score = score
            best_match = qa_pair['answer']
    
    return best_match if highest_score > 0 else "I don't have information about that specific topic. Please try rephrasing your question."

# Streamlit UI
def main():
    st.title("FST Tanger Mechanical Engineering Chatbot")
    
    # Language selector
    language = st.selectbox(
        "Select Language / Choisir la langue / اختر اللغة",
        ["English", "Français", "العربية"]
    )
    
    # Load knowledge bases
    kb_en, kb_fr, kb_ar = load_knowledge_base()
    
    # Select appropriate knowledge base based on language
    if language == "English":
        kb = kb_en
        placeholder_text = "Ask your question about Mechanical Engineering..."
        welcome_msg = "Welcome! I can help you with information about Mechanical Engineering at FST Tanger."
    elif language == "Français":
        kb = kb_fr
        placeholder_text = "Posez votre question sur le Génie Mécanique..."
        welcome_msg = "Bienvenue ! Je peux vous aider avec des informations sur le Génie Mécanique à la FST Tanger."
    else:
        kb = kb_ar
        placeholder_text = "...اطرح سؤالك حول الهندسة الميكانيكية"
        welcome_msg = "!مرحبا! يمكنني مساعدتك بمعلومات حول الهندسة الميكانيكية في كلية العلوم والتقنيات طنجة"

    st.write(welcome_msg)
    
    # User input
    user_question = st.text_input("", placeholder=placeholder_text)
    
    if user_question:
        response = get_best_response(user_question, kb)
        st.write("Response:", response)

if __name__ == "__main__":
    main()
