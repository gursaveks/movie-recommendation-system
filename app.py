import os

import pandas as pd
import requests
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


folder = os.path.dirname(os.path.abspath(__file__))
movies = pd.read_csv(os.path.join(folder, "movies.csv"))
ratings = pd.read_csv(
    os.path.join(folder, "ratings.csv"),
    usecols=["movieId", "rating"],
)
average_ratings = ratings.groupby("movieId")["rating"].mean()

movies["features"] = (
    movies["title"].fillna("")
    + " "
    + movies["genres"].fillna("").str.replace("|", " ", regex=False)
)
vectorizer = CountVectorizer(stop_words="english")
feature_matrix = vectorizer.fit_transform(movies["features"])


def find_movie(title):
    title = title.strip().lower()
    exact_match = movies[movies["title"].str.lower() == title]
    if not exact_match.empty:
        return exact_match.iloc[0]

    partial_match = movies[movies["title"].str.lower().str.contains(title, regex=False)]
    if not partial_match.empty:
        return partial_match.iloc[0]
    return None


def get_recommendations(movie):
    movie_index = movie.name
    scores = cosine_similarity(feature_matrix[movie_index], feature_matrix)[0]
    similar_movies = pd.Series(scores, index=movies.index).nlargest(6).iloc[1:]
    return movies.loc[similar_movies.index]


@st.cache_data(show_spinner=False)
def get_poster(title):
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        return None

    title_without_year = title.rsplit(" (", 1)[0]
    response = requests.get(
        "https://api.themoviedb.org/3/search/movie",
        params={"api_key": api_key, "query": title_without_year},
        timeout=10,
    )
    if response.status_code != 200:
        return None

    results = response.json().get("results", [])
    if not results or not results[0].get("poster_path"):
        return None
    return "https://image.tmdb.org/t/p/w500" + results[0]["poster_path"]


st.set_page_config(page_title="Movie Recommendations", page_icon="🎬", layout="wide")
st.title("Movie Recommendation System")
st.write("Find movies similar to your favorite movie, with posters and ratings.")

movie_title = st.text_input(
    "Enter a movie title",
    placeholder="For example: Avatar (2009)",
)

if st.button("Get Recommendations", type="primary"):
    if not movie_title.strip():
        st.warning("Please enter a movie title.")
    else:
        selected_movie = find_movie(movie_title)
        if selected_movie is None:
            st.error("Movie not found. Try another title.")
        else:
            st.subheader(f"Recommendations for {selected_movie['title']}")
            recommendations = get_recommendations(selected_movie)
            columns = st.columns(5)

            for column, (_, movie) in zip(columns, recommendations.iterrows()):
                with column:
                    poster = get_poster(movie["title"])
                    if poster:
                        st.image(poster, use_container_width=True)
                    else:
                        st.info("Poster unavailable")
                    st.markdown(f"**{movie['title']}**")
                    rating = average_ratings.get(movie["movieId"], 0)
                    st.write(f"Rating: {rating:.1f}/5")

if not os.getenv("TMDB_API_KEY"):
    st.caption("Set TMDB_API_KEY to display movie posters.")
