from flask_mongoengine import MongoEngine
import click
from flask.cli import with_appcontext
from flask import current_app


db = MongoEngine()

@click.command('delete-db')
@with_appcontext
def delete_db_command():
    """Delete existing db."""
    db_name = current_app.config['MONGODB_DB']
    db.connection.drop_database(db_name)
    click.echo('database deleted.')

def init_app(app):
    db.init_app(app)
    app.cli.add_command(delete_db_command)
