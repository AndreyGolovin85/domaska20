import pytest

from service.movie import MovieService


class TestMovieService:
	@pytest.fixture(autouse=True)
	def movie_service(self, movie_dao):
		self.movie_service = MovieService(dao=movie_dao)

	def test_get_one(self):
		movie = self.movie_service.get_one(1)
		assert movie is not None
		assert movie.id is not None
		assert movie.title == "My New Movie"
		assert isinstance(movie.id, int)

	def test_get_all(self):
		movie = self.movie_service.get_all()
		assert len(movie) > 0
		assert movie is not None

	def test_create(self):
		movie_info = {"title": "What you want?"}
		new_movie = self.movie_service.create(movie_info)
		assert new_movie is not None
		assert new_movie.id is not None
		assert new_movie.rating == 10  # Создаем фильм 'Movie_4' с рейтингом = 10

	def test_update(self):
		movie_d = {
			"id": 3,
			"title": "Just new film's title",
			"description": "Only for tests",
			"trailer": "Missing... =(",
			"year": 2017,
			"rating": 5,
			"genre_id": 2,
			"director_id": 3,
		}
		self.movie_service.update(movie_d)
		assert movie_d is not None

	def test_delete(self):
		result = self.movie_service.delete(1)
		assert result is None
