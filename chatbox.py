
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import streamlit as st

with open(r'C:\Users\toshiba\Desktop\datascience\chatbox\mobydick.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', ' ')

sentences = sent_tokenize(data)


def preprocess(sentence):
    words = word_tokenize(sentence)

    words = [word.lower() for word in words if
             word.lower() not in stopwords.words('english') and word not in string.punctuation]

    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

nltk.download('stopwords')
nltk.download('stopwords')

nltk.download('wordnet')

nltk.download('omw-1.4')

corpus = [preprocess(sentence) for sentence in sentences]

def get_most_relevant_sentence(query):
    query = preprocess(query)
    max_similarity = 0
    most_relevant_sentence = ""
    for sentence in corpus:
        similarity = len(set(query).intersection(sentence)) / float(len(set(query).union(sentence)))
        if similarity > max_similarity:
            max_similarity = similarity
            most_relevant_sentence = " ".join(sentence)
    return most_relevant_sentence

def chatbot(question):
    most_relevant_sentence = get_most_relevant_sentence(question)
    return most_relevant_sentence

import streamlit as st

def main():
    st.title("Chatbot")
    st.write("Hello! I'm a chatbot. Ask me anything about the topic in the text file.")
    # Get the user's question
    question = st.text_input("You:")
    # Create a button to submit the question
    if st.button("Submit"):
        # Call the chatbot function with the question and display the response
        response = chatbot(question)
        st.write("Chatbot: " + response)
if __name__ == "__main__":
    main()
