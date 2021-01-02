import base64
import unittest
from unittest.mock import patch

from werkzeug.exceptions import Unauthorized
from werkzeug.security import generate_password_hash

from mathapi.services.auth import login_required


class TestAuthService(unittest.TestCase):
    @patch("mathapi.services.auth.flask_restful")
    def test_login_required_unauthenticated(self, flask_restful):
        flask_restful.request.headers = {}
        with self.assertRaises(Unauthorized):
            login_required(lambda: "response")()

    @patch("mathapi.services.auth.users")
    @patch("mathapi.services.auth.flask_restful")
    def test_login_required_authenticated(self, flask_restful, users):
        users.return_value = {"test": generate_password_hash("password")}

        flask_restful.request.headers = {"Authorization": f"Basic {base64.b64encode(b'test:password').decode('utf-8')}"}
        response = login_required(lambda: "response")()
        assert response == "response"
