import pytest

from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director.name == "Тейлор Шеридан"

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) == 4

    def test_create(self):
        director_d = {"id": 4, "name": "Маня Маланя"}
        director = self.director_service.create(director_d)
        assert director.name == "Декстер Флетчер"
        assert director.id == 4


    def test_update(self):
        director_d = {"id": 4, "name": "Маня Маланя"}
        director = self.director_service.update(director_d)
        assert director is True

    def test_partial_update(self):
        director_d = {"id": 4, "name": "Маня Маланя"}
        director = self.director_service.partially_update(director_d)
        assert director is None

    def test_delete(self):
        director = self.director_service.delete(2)
        assert director is None





