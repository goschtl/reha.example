import importscan
import reha.example


def test_base(web_app):
    importscan.scan(reha.example)
    response = web_app.get('/')
    print(response)
    assert 1 == 1 
