# zlapi

## Important files:

- `config.py`: general settings are versioned.
- `instance/config.py`: specific settings override general settings and are ignored from the version control system.
- `.flaskenv`: flask specific configurations not versioned.
- `requirements.txt`: app dependencies.
- `.python-version`: specific version of python used for development.

## Install the app to production

It needs an environment wit python 3.8 and install dependencies:

    $ pip install -r requirements.txt

Copy `config.py`, `requirements.txt`, `.python-version` if using pyenv, and `.flaskenv` depending on the production server you are using.

Generate distributable file to make the application installable:

    $ python setup.py bdist_wheel

Copy this `dist/*.whl` file to the destination machine and install the application:

    $ pip install wheel
    $ pip install zlapi-0.1.2-py3-none-any.whl

Add specific setting for the production server. If using `venv`, you need to add the `config.py` in `venv/var/zlapi-instance/`. This file sets the following:

    SECRET_KEY='serious-key'
    DEBUG = False
    MONGODB_DB = 'zlapi'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017

Run the server:

    it depends on the chosen server.
