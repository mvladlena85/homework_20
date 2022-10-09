import pytest

from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre.name == "Комедия"

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) == 3

    def test_create(self):
        genre_d = {"id": 4, "name": "Маня Маланя"}
        genre = self.genre_service.create(genre_d)
        assert genre.name == "Драма"
        assert genre.id == 4

    def test_update(self):
        genre_d = {"id": 4, "name": "Маня Маланя"}
        genre = self.genre_service.update(genre_d)
        assert genre is True

    def test_partial_update(self):
        genre_d = {"id": 4, "name": "Маня Маланя"}
        genre = self.genre_service.partially_update(genre_d)
        assert genre is None

    def test_delete(self):
        genre = self.genre_service.delete(2)
        assert genre is None
