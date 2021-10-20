import importscan
import uvcreha
import pytest
from webtest import TestApp as WebApp
from uvcreha.app import Application
from reiter.contenttypes.registry import Registry
from reha.prototypes.contents import User, File, Document


@pytest.fixture(scope= 'class')
def application(request,
                user_interface,
                authentication,
                session_middleware,
                database_with_contents):

    contents = Registry()
    contents.register('user', User)
    contents.register('document', Document)
    contents.register('file', File)

    importscan.scan(uvcreha)
    app = Application(
        database=database_with_contents,
        authentication=authentication,
        ui=user_interface,
        contents=contents
    )
    request.cls.app = app
    request.cls.wsgi = WebApp(session_middleware(app))
    yield


@pytest.mark.usefixtures("application")
class TestApplication:

    def test_app(self):
        response = self.wsgi.get('/')
        assert response.status_int == 303
