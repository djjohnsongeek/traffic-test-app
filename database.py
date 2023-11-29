import click
from flask import current_app, g
from peewee import MySQLDatabase
from models import PageView

db_models = [PageView]

def get_db() -> MySQLDatabase:
    if 'db' not in g:
        config = current_app.config
        g.db = MySQLDatabase(
            config["DB_NAME"],
            user=config["DB_USER"],
            password=config["DB_PASSWORD"],
            host=config["DB_HOST"],
            port=config["DB_PORT"]
        )

        for model in db_models:
            model.bind(g.db)

    return g.db

def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    db.connect()

    # Prepare db schema
    db.drop_tables(db_models)
    db.create_tables(db_models)
    
    db.close()

def init_app(app):
    app.cli.add_command(init_db_command)
 
@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Database Initialized ...")