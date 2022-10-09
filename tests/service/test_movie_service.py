import pytest
from service.movie import MovieService


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id == 1

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) == 3

    def test_create(self):
        movie_d = {"id": 3,
                   "title": "Вооружен и очень опасен",
                   "description": "События происходят в конце XIX века на Диком Западе..",
                   "trailer": "https://www.youtube.com/watch?v=hLA5631F-jo",
                   "year": 1978,
                   "rating": 6,
                   "genre": 17,
                   "director": 3}

        movie = self.movie_service.create(movie_d=movie_d)
        assert movie.id == 3

    def test_update(self):
        movie_d = {"id": 3,
                   "title": "Вооружен и очень опасен22222",
                   "description": "События происходят в конце XIX века на Диком Западе..",
                   "trailer": "https://www.youtube.com/watch?v=hLA5631F-jo",
                   "year": 1976,
                   "rating": 8,
                   "genre": 16,
                   "director": 6}

        movie = self.movie_service.update(movie_d=movie_d)
        assert movie.id is not None



    def test_partial_update(self):
        movie_d = {"id": 3,
                   "title": "Вооружен и очень опасен22222",
                   "description": "События происходят в конце XIX века на Диком Западе..",
                   "director": 6}

        movie = self.movie_service.partially_update(movie_d=movie_d)


class TestMovieServiceNeg:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_neg):
        self.movie_service = MovieService(dao=movie_dao_neg)

    def test_update_negative(self):
        movie_d = {"id": 3,
                   "title": "Вооружен и очень опасен22222",
                   "description": "События происходят в конце XIX века на Диком Западе..",
                   "rating": 8,
                   "genre": 16,
                   "director": 6}

        with pytest.raises(Exception):
            movie = self.movie_service.partially_update(movie_d=movie_d)


