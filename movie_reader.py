# Taking movie data and printing 10 random titles based on release date
# JGullbrand - January 30th, 2019

import json
import random

with open("movies.json") as json_file:
	movie_list = json.load(json_file)
#this data was pulled from the github acct mentioned in the readme file	

movie_titles = []
#empty list to store the movie titles
while True:
#runs unless somenone types 'q' to break the loop	
	prompt = ("what year would you like to see a list of movies from? Please enter year as yyyy or type 'q' to exit \n> ")
	#adding in a bit of interactivity
	response = input(prompt)
	try:
		if response == 'q':
			break
		else:	
			for movie_info in movie_list:
				if movie_info["year"] == int(response):
					movie_titles.append(movie_info["title"])
			random.shuffle(movie_titles)
			#shuffles the list of movie_titles
			for movies in movie_titles[:10]:
			#taking 10 movies from the list	
				print(movies)	
	except ValueError:
	# just in case someone types in 'two thousand and six' or another string, rather than 2006
		print("Please enter in the year in the format yyyy (2018, for example)")
		continue