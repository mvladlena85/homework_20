import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    dir1 = Director(id=1, name="Тейлор Шеридан")
    dir2 = Director(id=2, name="Квентин Тарантино")
    dir3 = Director(id=3, name="Владимир Вайншток")
    dir4 = Director(id=4, name="Декстер Флетчер")

    director_dao.get_one = MagicMock(return_value=dir1)
    director_dao.get_all = MagicMock(return_value=[dir1, dir2, dir3, dir4])
    director_dao.create = MagicMock(return_value=dir4)
    director_dao.update = MagicMock(return_value=True)
    director_dao.delete = MagicMock(return_value=True)

    return director_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(id=1, title="Йеллоустоун",
                   description="Владелец ранчо пытается сохранить землю своих предков.", trailer="https://www.youtube.com/watch?v=UKei_d0cbP4",
                   year=2018, rating=8.6,
                   genre_id=17, director_id=1)
    movie2 = Movie(id=2, title="Омерзительная восьмерка",
                   description="США после Гражданской войны.", trailer="https://www.youtube.com/watch?v=lmB9VWm0okU",
                   year=2015, rating=7.8,
                   genre=4, director=2)
    movie3 = Movie(id=3, title="Вооружен и очень опасен",
                   description="События происходят в конце XIX века на Диком Западе..", trailer="https://www.youtube.com/watch?v=hLA5631F-jo",
                   year=1978, rating=6,
                   genre=17, director=3)

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=movie3)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao

@pytest.fixture()
def movie_dao_neg():
    movie_dao = MovieDAO(None)

    movie_dao.update = MagicMock(side_effect=Exception("the list is not full"))

    return movie_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre1 = Genre(id=1, name="Комедия")
    genre2 = Genre(id=2, name="Семейный")
    genre3 = Genre(id=3, name="Фэнтези")
    genre4 = Genre(id=4, name="Драма")

    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    genre_dao.create = MagicMock(return_value=genre4)
    genre_dao.update = MagicMock(return_value=True)
    genre_dao.delete = MagicMock()

    return genre_dao

