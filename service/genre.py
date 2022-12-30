from dao.genre import GenreDAO


class GenreService:
	def __init__(self, dao: GenreDAO):
		self.dao = dao

	def get_one(self, bid):
		return self.dao.get_one(bid)

	def get_all(self):
		return self.dao.get_all()

	def create(self, genre_d):
		return self.dao.create(genre_d)

	def update(self, genre_d):
		if not isinstance(genre_d["id"], int):
			raise Exception("Genre's id must be only INTEGER type!")

		if not isinstance(genre_d["name"], str):
			raise Exception("Genre's name must be only STRING type!")

		return self.dao.update(genre_d)

	def partially_update(self, genre_d):
		genre = self.get_one(genre_d["id"])
		if "name" in genre_d:
			genre.name = genre_d.get("name")
		self.dao.update(genre)

	def delete(self, rid):
		if not isinstance(rid, int):
			raise Exception("'Genre_id' must be only INTEGER number!")
		self.dao.delete(rid)
