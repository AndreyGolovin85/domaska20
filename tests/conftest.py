from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie


@pytest.fixture()
def director_dao():
	director_dao = DirectorDAO(None)  # DirectorDAO из DAO

	# Director из DAO -> model
	director_1 = Director(id=1, name="Charles")
	director_2 = Director(id=2, name="Max")
	director_3 = Director(id=3, name="Carlos")
	director_4 = Director(id=4, name="Sergio")

	director_dao.get_one = MagicMock(return_value=director_1)
	director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
	director_dao.create = MagicMock(return_value=director_4)
	director_dao.update = MagicMock()
	director_dao.delete = MagicMock()

	return director_dao


@pytest.fixture()
def genre_dao():
	genre_dao = GenreDAO(None)  # GenreDAO из DAO

	# Genre из DAO -> model
	genre_1 = Genre(id=1, name="Fantasy Comedy")
	genre_2 = Genre(id=2, name="Historical")
	genre_3 = Genre(id=3, name="Biological")
	genre_4 = Genre(id=4, name="Old cartoons")

	genre_dao.get_one = MagicMock(return_value=genre_1)
	genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
	genre_dao.create = MagicMock(return_value=genre_4)
	genre_dao.update = MagicMock()
	genre_dao.delete = MagicMock()

	return genre_dao


@pytest.fixture()
def movie_dao():
	movie_dao = MovieDAO(None)  # MovieDAO из DAO

	# Movie из DAO -> model
	movie_1 = Movie(id=1, title="My New Movie", description="My first Movie", trailer="https://skyengpublic.notion.site/20-c-Flask-8b2971cefa5c4ef6a2a8b510df0420bd", year=2022, rating=8, genre_id=1, director_id=3)
	movie_2 = Movie(id=2, title="PyCharm's lessons", description="Necessary lessons in PyCharm", trailer="https://www.youtube.com/watch?v=1DfFJNEfXpY", year=2020, rating=9, genre_id=4, director_id=2)
	movie_3 = Movie(id=3, title="A little about Python", description="History about Python", trailer="https://www.youtube.com/watch?v=LFCq-mNF96c", year=2021, rating=10, genre_id=3, director_id=4)
	movie_4 = Movie(id=4, title="Flask & Django: friends or enemies =)", description="A few jokes", trailer="None", year=2010, rating=10, genre_id=5, director_id=1)

	movie_dao.get_one = MagicMock(return_value=movie_1)
	movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
	movie_dao.create = MagicMock(return_value=movie_4)
	movie_dao.update = MagicMock()
	movie_dao.delete = MagicMock()

	return movie_dao






















