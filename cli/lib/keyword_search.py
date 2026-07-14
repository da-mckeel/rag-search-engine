import string
from .search_utils import load_movies, DEFAULT_SEARCH_LIMIT

def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    for m in movies:
        pproc_query = preprocess_text(query)
        pproc_title = preprocess_text(m["title"])
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