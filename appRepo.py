from models import PageView
from datetime import datetime


def log_view(user_uuid: str, source: str, page: str):
    PageView.insert(
        timestamp = datetime.now(),
        page = page,
        user_uuid = user_uuid,
        source = source
    ).execute()

# select site views, determin how many are unique
def site_views():
    result = PageView.select(PageView, fn.Count(PageView.user_uuid).alias("count")).group_by(PageView.user_uuid).execute()

# select all views, group by source, determine count for reach source

# select index page views, determine how many are unique

# select reports page views, determine how many are unique