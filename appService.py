from flask import current_app, session, Request
import uuid
import appRepo

def get_user_id():
    config = current_app.config

    userId = session.get(config["USER_COOKIE_KEY"], None)

    if userId is None:
        session[config["USER_COOKIE_KEY"]] = str(uuid.uuid4())
        userId = session[config["USER_COOKIE_KEY"]]
    
    return userId

def capture_page_view(request: Request, page: str):
    source = request.args.get("source", "other")
    if source not in current_app.config["SOURCES"]:
        source = "other"

    user_id = get_user_id()

    appRepo.log_view(user_id, source, page)