import json
import os

DEFAULT_SEARCH_LIMIT = 5
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")
STOP_WORDS = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")

def load_movies():
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data["movies"]

def load_stop_words():
    with open(STOP_WORDS, "r") as f:
        data = f.read()
        word_list = data.splitlines()
    return word_list