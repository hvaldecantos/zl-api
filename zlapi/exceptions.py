from werkzeug.exceptions import HTTPException


class ZlapiBaseException(HTTPException):
    pass

class InvalidCredentials(ZlapiBaseException):
    code = 401
    description = 'Invalid credentials.'
