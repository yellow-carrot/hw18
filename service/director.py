from dao.director import DirectorDAO


class DirectorService:
    def __int__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()
