# Movie Recommendation System

A simple content-based movie recommendation project built with Python. It compares movie titles and genres, finds similar movies, and displays their average ratings from the MovieLens dataset.

## Project Overview

The program takes one or more movie titles as input. For each title, it compares the movie's genre information with all other movies and returns the five most similar results. A movie's average user rating is shown beside each recommendation.

This project is designed as a clear command-line example for learning about:

- Reading CSV files with pandas
- Grouping ratings and calculating averages
- Converting text into numerical features
- Comparing movies with cosine similarity
- Building a small interactive Python program

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

The current dataset does not contain poster URLs or image IDs, so the command-line version displays movie titles and ratings. Poster support can be added later by connecting the project to a movie metadata service such as TMDB and adding a poster URL for each movie.
