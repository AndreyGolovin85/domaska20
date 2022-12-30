from dao.director import DirectorDAO


class DirectorService:
	def __init__(self, dao: DirectorDAO):
		self.dao = dao

	def get_one(self, bid):
		return self.dao.get_one(bid)

	def get_all(self):
		return self.dao.get_all()

	def create(self, director_d):
		return self.dao.create(director_d)

	def update(self, director_d):
		if not isinstance(director_d["id"], int):
			raise Exception("Director's id must be only INTEGER type!")

		if not isinstance(director_d["name"], str):
			raise Exception("Director's name must be only STRING type!")

		return self.dao.update(director_d)

	def partially_update(self, director_d):
		director = self.get_one(director_d["id"])
		if "name" in director_d:
			director.name = director_d.get("name")
		self.dao.update(director)

	def delete(self, rid):
		if not isinstance(rid, int):
			raise Exception("'Director_id' must be only INTEGER number!")
		self.dao.delete(2)
