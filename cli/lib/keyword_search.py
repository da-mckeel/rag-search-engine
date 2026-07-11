import string
from .search_utils import load_movies, DEFAULT_SEARCH_LIMIT

def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    for m in movies:
        pproc_query = preprocess_text(query)
        pproc_title = preprocess_text(m["title"])
        if pproc_query in pproc_title:
            results.append(m)
            if len(results) >= limit:
                break
    return results

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = text.translate(str.maketrans("","",string.punctuation))
    return text