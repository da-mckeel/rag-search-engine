import string
from tracemalloc import stop
from .search_utils import load_movies, DEFAULT_SEARCH_LIMIT, load_stop_words

def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    stop_words = load_stop_words()
    pproc_stop_words = preprocess_stop_words(stop_words)
    results = []
    for m in movies:
        pproc_query = remove_stop_words(preprocess_text(query), pproc_stop_words)
        pproc_title = remove_stop_words(preprocess_text(m["title"]), pproc_stop_words)
        found = False
        for word in pproc_query:
            for title_word in pproc_title:
                if word in title_word:
                    results.append(m)
                    found = True
                    break
            if found:
                break
        if len(results) >= limit:
            break
    return results

def preprocess_text(text: str) -> list:
    text = text.lower()
    text = text.translate(str.maketrans("","",string.punctuation))
    text_list = text.split()
    return text_list



def preprocess_stop_words(list) -> list:
    text_list = []
    for l in list:
        l = l.lower()
        l = l.translate(str.maketrans("","",string.punctuation))
        text_list.append(l)
    return text_list


def remove_stop_words(tokens, stop_words):
    cleaned_words = []
    for t in tokens:
        if t not in stop_words:
            cleaned_words.append(t)
    return cleaned_words