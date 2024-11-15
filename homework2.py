#დავალება N2

import json
from datetime import datetime

def process_movies(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)

    processed_movies = []

    for movie in data:
        release_year = int(movie["release_date"].split("-")[0])
        genres = movie["genres"]

        if release_year > 2000 and "Crime" in genres:
            movie["genres"] = [genre.replace("Crime", "New_Crime") for genre in genres]
            processed_movies.append(movie)
        elif release_year < 2000 and "Drama" in genres:
            movie["genres"] = [genre.replace("Drama", "Old_Drama") for genre in genres]
            processed_movies.append(movie)
        elif release_year == 2000:
            movie["genres"].append("New_Century")
            processed_movies.append(movie)

    with open(file_name, 'w') as file:
        json.dump(processed_movies, file, indent=4)

file_name = "movies.json"
process_movies(file_name)
print(f"Movies have been processed and saved back to {file_name}.")
