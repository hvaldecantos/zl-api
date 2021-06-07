from tests.base_case import BaseCase
from flask import jsonify

class AppTest(BaseCase):

    def test_initial_endpoint(self):
        # Given the app

        # When
        response = self.app.get('/api/')

        # Then
        assert response.json['message'] == 'Initial api structure deployed.'
        assert response.status_code == 200

    def test_page_not_found(self):
        # Given the app

        # When
        response = self.app.get('/api/non-existent-endpoint')

        # Then
        assert response.json['error'] == 'Resource not found.'
        assert response.status_code == 404
