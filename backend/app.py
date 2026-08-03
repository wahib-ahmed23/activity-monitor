from fastapi import FastAPI
from sqlalchemy import select

from backend.database import SessionLocal
from backend.models import Activity

app = FastAPI(
    title="Activity Monitor API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Welcome to Activity Monitor"
    }


@app.get("/health")
def health():
    return {
        "healthy": True
    }


@app.get("/activities")
def get_activities():
    db = SessionLocal()

    activities = db.scalars(
        select(Activity)
    ).all()

    data = []

    for activity in activities:
        data.append({
            "id": activity.id,
            "process": activity.process,
            "window_title": activity.window_title,
            "start_time": activity.start_time,
            "end_time": activity.end_time,
            "duration": activity.duration
        })

    db.close()

    return data