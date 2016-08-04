from sys import argv
from media import Movie
import fresh_tomatoes
import json

#Read movie data from a source JSON file if it's supplied, otherwise default to demo.json
filename = argv[1] if len(argv) > 1 else 'demo.json'

with open(filename,'r') as infile:
    movie_data_list = json.load(infile)

movie_list = [Movie(data) for data in movie_data_list]
fresh_tomatoes.open_movies_page(movie_list)


