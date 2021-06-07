import json
from zlapi.database.models import User
from tests.base_case import BaseCase
from flask_bcrypt import check_password_hash

class TestAuthSuite(BaseCase):
    name = 'someone'
    password = "apassword"
    email = "someone@server.com"

    def test_encrypted_password(self):
        # Given
        payload = json.dumps({
            "name": self.name,
            "email": self.email,
            "password": self.password
        })

        # When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        user = User.objects.get(id=response.json['id'])

        # Then
        assert check_password_hash(user.password, self.password)

    def test_successful_signup(self):
        # Given
        payload = json.dumps({
            "name": "paurakh",
            "email": "paurakh011@gmail.com",
            "password": "mycoolpassword"
        })

        # When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        assert str == type(response.json['id'])
        assert 200 == response.status_code

    def test_successful_login(self):
        # Given
        payload = json.dumps({
            "name": self.name,
            "email": self.email,
            "password": self.password
        })
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # When
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        assert str == type(response.json['token'])
        assert 200 == response.status_code
