from models import PageView
from datetime import datetime


def log_view(user_uuid: str, source: str, page: str):
    try:
        PageView.insert(
            timestamp = datetime.now(),
            page = page,
            user_uuid = user_uuid,
            source = source
        ).execute()
    except:
        pass