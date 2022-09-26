import src.flask_instance as fi


def test_app():
    fi.app.config['TESTING'] = True
    assert fi.app is not None
