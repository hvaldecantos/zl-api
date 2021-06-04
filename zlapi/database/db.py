from flask_mongoengine import MongoEngine
import click
from flask.cli import with_appcontext


db = MongoEngine()

@click.command('delete-db')
@with_appcontext
def delete_db_command():
    """Delete existing db."""
    db.connection.drop_database("zl-api")
    click.echo('database deleted.')

def init_app(app):
    db.init_app(app)
    app.cli.add_command(delete_db_command)
