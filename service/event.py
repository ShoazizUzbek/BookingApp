from typing import Optional

from sqlalchemy.orm import Session

from database.models import Event


class EventService():

    def all_events(self, db):
        return db.query(Event).all()

    def get_by_id(self, db, id: int) -> Optional[Event]:
        return db.query(Event).filter(Event.id == id).first()

    def create(self, db, data) -> Optional[Event]:
        db_obj = Event(
            **data
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

event_service = EventService()