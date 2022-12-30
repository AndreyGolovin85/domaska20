from dao.movie import MovieDAO


class MovieService:
	def __init__(self, dao: MovieDAO):
		self.dao = dao

	def get_one(self, bid):
		return self.dao.get_one(bid)

	def get_all(self):
		return self.dao.get_all()

	def create(self, movie_d):
		return self.dao.create(movie_d)

	def update(self, movie_d):
		if not isinstance(movie_d["id"], int):
			raise Exception("'Movie_id' must be only INTEGER type!")

		if not isinstance(movie_d["title"], str):
			raise Exception("'Movie_title' must be only STRING type!")

		if not isinstance(movie_d["description"], str):
			raise Exception("'Movie_description' must be only STRING type!")

		if not isinstance(movie_d["trailer"], str):
			raise Exception("'Movie_trailer' must be only STRING type!")

		if not isinstance(movie_d["year"], int):
			raise Exception("'Movie_year' must be only INTEGER type!")

		if not isinstance(movie_d["rating"], int):
			raise Exception("'Movie_rating' must be only INTEGER type!")

		if not isinstance(movie_d["genre_id"], int):
			raise Exception("'Movie_genre_id' must be only INTEGER type!")

		if not isinstance(movie_d["director_id"], int):
			raise Exception("'Movie_director_id' must be only INTEGER type!")

		return self.dao.update(movie_d)

	def partially_update(self, movie_d):
		movie = self.get_one(movie_d["id"])
		if "title" in movie_d:
			movie.title = movie_d.get("title")
		if "description" in movie_d:
			movie.description = movie_d.get("description")
		if "trailer" in movie_d:
			movie.trailer = movie_d.get("trailer")
		if "year" in movie_d:
			movie.year = movie_d.get("year")
		if "rating" in movie_d:
			movie.rating = movie_d.get("rating")
		if "genre_id" in movie_d:
			movie.genre_id = movie_d.get("genre_id")
		if "director_id" in movie_d:
			movie.director_id = movie_d.get("director_id")
		self.dao.update(movie)

	def delete(self, rid):
		if not isinstance(rid, int):
			raise Exception("'Movie_id' must be only INTEGER number!")
		self.dao.delete(rid)
