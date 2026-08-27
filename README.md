# Movie Recommendation System

A beginner-friendly Python project that recommends similar movies using movie genres and ratings from the MovieLens dataset.

## Features

- Finds five movies similar to a selected movie
- Uses movie genres to compare movies
- Displays the average rating for each recommendation
- Uses a simple command-line interface

## Project Files

| File | Description |
| --- | --- |
| `Movie Recomendation system.py` | Main Python program |
| `movies.csv` | Movie titles and genres |
| `ratings.csv` | Movie ratings used by the program |
| `requirements.txt` | Required Python packages |

## Setup

1. Install Python 3.10 or newer.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the MovieLens dataset from [GroupLens](https://grouplens.org/datasets/movielens/).
4. Place `ratings.csv` in the same folder as the Python file.
5. Run the program:

   ```bash
   python "Movie Recomendation system.py"
   ```

6. Enter a movie title exactly as it appears in `movies.csv`, for example:

   ```text
   Avatar (2009)
   ```

## Example

```text
Movie Recommendation System
Enter the exact movie title, such as Avatar (2009): Avatar (2009)

Recommended movies:
Star Trek (2009) (rating: 3.8/5)
```

## Note About `ratings.csv`

The full ratings file is too large for a normal GitHub repository, so it is excluded through `.gitignore`. Download it separately before running the program.
