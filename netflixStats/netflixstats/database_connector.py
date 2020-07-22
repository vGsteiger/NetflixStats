from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
import pathlib

from .models import Movie, Series


Base = declarative_base()
path_to_db = pathlib.Path(__file__).parent.absolute()


class DatabaseConnection:

    def __init__(self):
        db = 'sqlite:///{}'.format(path_to_db)
        print(db)
        self.engine = create_engine(db, echo=True)
        Base.metadata.create_all(self.engine)

    def add_movie(self, movie):
        with self.session_scope() as session:
            obj = DBMovie(name='Test', password='test')
            session.add(obj)

    def init_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.init_session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            return -1
        finally:
            session.close()


class DBMovie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'User {self.name}'
