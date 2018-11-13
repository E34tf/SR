import pandas as pd

# import numpy as np
# import random

# Importing all data
movies_data = pd.read_csv('ml/movies.csv', sep=',')
ratings_data = pd.read_csv('ml/ratings.csv', sep=',')
tags_data = pd.read_csv('ml/tags.csv', sep=',')
links_data = pd.read_csv('ml/links.csv', sep=',')
genome_scores_data = pd.read_csv('ml/genome-scores_csv', sep=',')
genome_tags_data = pd.read_csv('ml/genome-tags.csv', sep=',')

# Genres data
genre_labels = set()
for s in movies_data['genres'].str.split('|').values:
    genre_labels = genre_labels.union(set(s))

# Cleaning timestamps
del ratings_data['timestamp']
del tags_data['timestamp']

# Cleaing null rows
tags_data = tags_data.dropna()

# Inner Joins on tables
movie_ratings_data = movies_data.merge(ratings_data, on = 'movieId', how = 'inner')

print('\n\n')


from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()
rows = session.execute('SELECT name, age, email FROM users')
for user_row in rows:
    print(user_row.name, user_row.age, user_row.email)