from flask import Flask, request, render_template, current_app, session
from database import init_db_command, get_db, close_db
import appService
import uuid

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = "dev",
    DB_NAME = "traffic_app",
    DB_USER = "root",
    DB_PASSWORD = "admin",
    DB_HOST = "localhost",
    DB_PORT = 3306,
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
    appService.capture_page_view(request, "index")
    return render_template("index.html")


@app.route("/reports", methods=["GET"])
def reports():
    appService.capture_page_view(request, "reports")
    return render_template("reports.html")