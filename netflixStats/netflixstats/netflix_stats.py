from .extract import Extractor
from .database_connector import DatabaseConnection


class NetflixStats:

    def __init__(self, print_out, run, file):
        filename = file
        self.print_out = print_out
        self.run = run
        # self.extractor = Extractor(filename)
        self.db_connector = DatabaseConnection()
        self.db_connector.add_movie(movie='Test')
