from dao.movie import MovieDAO


class MovieService:

    dao = MovieDAO

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, filters):
        if filters.get('director_id') is not None:
            movies = self.dao.get_by_director_id(filters.get('director_id'))

        elif filters.get('genre_id') is not None:
            movies = self.dao.get_by_genre_id(filters.get('genre_id'))

        elif filters.get('year') is not None:
            movies = self.dao.get_by_year(filters.get('year'))

        else:
            movies = self.dao.get_all()

        return movies

    def create(self, movie_dict):
        return self.dao.create(movie_dict)

    def update(self, movie_dict):
        self.dao.update(movie_dict)
        return self.dao

    def delete(self, mid):
        self.dao.delete(mid)
