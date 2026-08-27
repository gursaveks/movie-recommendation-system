# Movie Recommendation System

A simple content-based movie recommendation project built with Python. It compares movie titles and genres, finds similar movies, and displays their average ratings from the MovieLens dataset.

## Project Overview

The program takes one or more movie titles as input. For each title, it compares the movie's genre information with all other movies and returns the five most similar results. A movie's average user rating is shown beside each recommendation.

The project includes both a command-line program and a visual Streamlit web app. The web app shows recommendation cards with movie posters and ratings.

This project is designed as a clear example for learning about:

- Reading CSV files with pandas
- Grouping ratings and calculating averages
- Converting text into numerical features
- Comparing movies with cosine similarity
- Building a small interactive Python program
- Creating a simple web interface with Streamlit
- Loading poster images from a movie metadata API

## Features

- Recommend five similar movies
- Search using an exact or partial movie title
- Enter multiple movie titles in one run
- Display average ratings out of 5
- Use a simple command-line interface

## How It Works

1. `movies.csv` is loaded with movie titles and genres.
2. `ratings.csv` is grouped by `movieId` to calculate average ratings.
3. The title and genres are combined into one text field.
4. `CountVectorizer` converts the text into numerical features.
5. Cosine similarity compares the selected movie with the other movies.
6. The five highest similarity results are displayed.

## Project Files

| File | Description |
| --- | --- |
| `Movie Recomendation system.py` | Main Python application |
| `app.py` | Streamlit web application with poster cards |
| `movies.csv` | Movie IDs, titles, and genres |
| `ratings.csv` | User ratings for movies |
| `requirements.txt` | Required Python packages |

## Installation

1. Install Python 3.10 or newer.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python "Movie Recomendation system.py"
   ```

## Run the Web App

The visual version displays each recommendation with its poster, title, and rating.

1. Create a free API key at [TMDB](https://www.themoviedb.org/settings/api).
2. Set the key in PowerShell for the current terminal:

   ```powershell
   $env:TMDB_API_KEY = "your_tmdb_api_key"
   ```

3. Start Streamlit:

   ```bash
   streamlit run app.py
   ```

4. Open the local URL shown in the terminal.

## Usage

Enter one title:

```text
Avatar (2009)
```

Or enter multiple titles separated by semicolons:

```text
Avatar (2009); Star Trek Beyond (2016); Toy Story (1995)
```

The program also accepts a recognizable part of a title, such as `Trek Beyond (2016)`.

## Example Output

```text
Movie Recommendation System
Enter one or more movie titles separated by commas: Avatar (2009)

Recommendations for Avatar (2009):
Star Trek (2009) (rating: 3.8/5)
Transformers: Revenge of the Fallen (2009) (rating: 2.7/5)
```

## Dataset

This project uses the MovieLens dataset. The movie data contains the following columns:

- `movieId`: Unique movie identifier
- `title`: Movie title and release year
- `genres`: Pipe-separated movie genres

The ratings data contains:

- `userId`: Unique user identifier
- `movieId`: Movie identifier
- `rating`: User rating from 0.5 to 5.0

## Poster Support

The Streamlit app searches TMDB for each recommended movie and displays the available poster. The command-line version continues to display movie titles and ratings. If a poster is not available, the app shows a clear placeholder instead.
