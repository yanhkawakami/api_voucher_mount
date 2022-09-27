import main as main
from flask import Flask
import unittest


class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

    def test_show_message(self):
        with self.app.app_context():
            r = main.showMessage()
            assert r.status_code == 404
