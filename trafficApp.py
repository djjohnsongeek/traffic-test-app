from flask import Flask, request, render_template, current_app, session
from database import init_db_command, get_db, close_db
from appRepo import log_view
import uuid

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = "dev",
    DB_NAME = "traffic_app",
    DB_USER = "root",
    DB_PASSWORD = "",
    DB_HOST = "localhost",
    DB_PORT = 3308,
    SOURCES = ["reddit", "discord", "other", "facebook", "twitter", "youtube"],
    USER_COOKIE_KEY = "ta-user-id"
)

app.cli.add_command(init_db_command)

@app.before_request
def before_each_request():
    get_db()

@app.after_request
def after_each_request(response):
    close_db()
    return response

@app.route("/", methods=["GET"])
def index():
    source = request.args.get("source", "other")
    if source not in current_app.config["SOURCES"]:
        source = "other"

    page = "index"
    user_id = get_user_id()

    log_view(user_id, source, page)

    return render_template("index.html")


@app.route("/reports", methods=["GET"])
def reports():
    return render_template("reports.html")


def get_user_id():
    config = current_app.config

    userId = session.get(config["USER_COOKIE_KEY"], None)

    if userId is None:
        session[config["USER_COOKIE_KEY"]] = str(uuid.uuid4())
        userId = session[config["USER_COOKIE_KEY"]]
    
    return userId