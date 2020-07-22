from imdb import IMDb
import pandas as pd
from .database_connector import DatabaseConnection
import numpy as np
from datetime import datetime


class Extractor:

    def __init__(self, filename):
        self.filename = filename
        self.database_connection = DatabaseConnection()

    def extract(self):
        col_list = ['Title', 'Date']
        df = pd.read_csv(self.filename, usecols=col_list)
        ia = IMDb()
        series_dict = {}
        try:
            while i < len(df['Title']):
                date = df['Date'].iloc[i]
                if ':' in df['Title'].iloc[i]:
                    split_movie = df['Title'].iloc[i].split(':', 1)
                    series_name = split_movie[0]
                    movie = ia.search_movie(split_movie[1])
                    try:
                        first_match = movie[0]
                    except IndexError:
                        if series_name in series_dict:
                            t = series_dict.get(series_name)
                            runtime = int(t[1]) // int(t[0])
                            movie_list[i][0] = date
                            movie_list[i][1] = series_name
                            movie_list[i][2] = runtime
                            movie_list[i][3] = 'Series'
                        i += 1
                        continue
                    ia.update(first_match)
                    # ia.update(first_match, 'runtimes')
                    try:
                        runtime = int(first_match['runtimes'][0])
                    except KeyError:
                        i += 1
                        continue
                    movie_list[i][0] = date
                    movie_list[i][1] = series_name
                    movie_list[i][2] = runtime
                    movie_list[i][3] = 'Series'
                    if series_name in series_dict:
                        t = series_dict.get(series_name)
                        n = t[0] + 1
                        runtime = runtime + t[1]
                        series_dict.update({series_name: (n, runtime)})
                    else:
                        t = (1, runtime)
                        series_dict.update({series_name: t})
                else:
                    movie_name = df['Title'].iloc[i]
                    movie = ia.search_movie(movie_name)
                    first_match = movie[0]
                    ia.update(first_match)
                    try:
                        runtime = int(first_match.get('runtimes')[0])
                    except TypeError:
                        i += 1
                        continue
                    movie_list[i][0] = date
                    movie_list[i][1] = movie_name
                    movie_list[i][2] = runtime
                    movie_list[i][3] = 'Movie'
                print(movie_list[i][1])
                i += 1
        except KeyboardInterrupt:
            pass
