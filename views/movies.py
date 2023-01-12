from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema

from implemented import movie_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MovieView(Resource):
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre')
        year = request.args.get('year')

        filters = {
            'director_id': director,
            'genre_id': genre,
            'year': year

        }

        all_movies = movie_service.get_all(filters)
        result = MovieSchema(many=True).dump(all_movies)
        return result, 200

    def post(self):
        request_json = request.json
        movie = movie_service.create(request_json)
        return 'created', 201, {'location': f'/movies/{movie.id}'}


@movies_ns.route('/<int:mid>')
class MoviesView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return MovieSchema().dump(movie), 200

    def put(self, mid):
        request_json = request.json
        if 'id' not in request_json:
            request_json['id'] = mid
        movie_service.update(request_json)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return 'deleted', 204
