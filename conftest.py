import pytest

from python_training.fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    # создание объекта типа Application
    fixture = Application()
    # разрушение фикстуры
    request.addfinalizer(fixture.destroy)
    return fixture
