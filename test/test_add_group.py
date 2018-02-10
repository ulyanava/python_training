# -*- coding: utf-8 -*-

import pytest

from python_training.fixture.application import Application
from python_training.model.group import Group


@pytest.fixture
def app(request):
    # создание объекта типа Application
    fixture = Application()
    # разрушение фикстуры
    request.addfinalizer(fixture.destroy)

    return fixture


def test_add_group2(app):
    app.session.login(username="admin", password="secret")
    app.create_group_form(Group(name="name", header="header", footer="footer"))
    app.session.logout()
