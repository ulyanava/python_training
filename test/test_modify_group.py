from python_training.model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="name_modified", header="header_modified", footer="footer_modified"))
    app.session.logout()
