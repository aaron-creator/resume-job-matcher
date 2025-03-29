from flask import Flask, request, jsonify
import spacy
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#load NPL model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

def preprocess_text(text):
    text = text.lower()                         #to lower case
    text = re.sub(r'[^a-zA-Z0-9 ]','',text)     #Remove Special Characters
    doc = nlp(text)                             #text is passed through an NLP pipeline
    # lemma creats base fom of tokens. Stopwords are removed.
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    print("Tokens : ",tokens)
    return "".join(tokens)                      #Joins the tokens with Spaces.

@app.route("/match", methods=["POST"])          # routing for resume upload URL.