from datetime import datetime

from backend.database import SessionLocal
from backend.models import Activity


class ActivityService:

    def __init__(self):
        self.db = SessionLocal()

    def start_activity(self, process, title):

        activity = Activity(
            process=process,
            window_title=title,
            start_time=datetime.now()
        )

        self.db.add(activity)
        self.db.commit()
        self.db.refresh(activity)

        return activity