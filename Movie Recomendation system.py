import os

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


folder = os.path.dirname(os.path.abspath(__file__))
movies = pd.read_csv(os.path.join(folder, "movies.csv"))
ratings_file = os.path.join(folder, "ratings.csv")

if not os.path.exists(ratings_file):
    raise FileNotFoundError(
        "ratings.csv is missing. Download the MovieLens ratings file and place it in this folder."
    )

ratings = pd.read_csv(ratings_file, usecols=["movieId", "rating"])

movies["combined_features"] = (
    movies["title"].fillna("") + " " + movies["genres"].fillna("").str.replace("|", " ")
)

average_ratings = ratings.groupby("movieId")["rating"].mean()

vectorizer = CountVectorizer(stop_words="english")
feature_matrix = vectorizer.fit_transform(movies["combined_features"])


def recommend(movie_title):
    movie_rows = movies[movies["title"].str.lower() == movie_title.lower()]

    if movie_rows.empty:
        movie_rows = movies[movies["title"].str.lower().str.contains(movie_title.lower(), regex=False)]

    if movie_rows.empty:
        print("Movie not found. Try entering another title.")
        return

    movie_index = movie_rows.index[0]
    selected_movie = feature_matrix[movie_index]
    scores = cosine_similarity(selected_movie, feature_matrix)[0]

    movie_scores = list(enumerate(scores))
    movie_scores.sort(key=lambda item: item[1], reverse=True)

    print("\nRecommended movies:")
    for index, score in movie_scores[1:6]:
        movie = movies.iloc[index]
        average_rating = average_ratings.get(movie["movieId"], 0)
        print(f"{movie['title']} (rating: {average_rating:.1f}/5)")


if __name__ == "__main__":
    print("Movie Recommendation System")
    title = input("Enter the exact movie title, such as Avatar (2009): ").strip()
    recommend(title)
