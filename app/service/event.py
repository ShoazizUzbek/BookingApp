from typing import Optional

from sqlalchemy.orm import Session

from app.database.models import  Event



class EventService():

    def all_events(self, db: Session):
        return db.query(Event).all()

    def get_by_id(self, db: Session, id: int) -> Optional[Event]:
        return db.query(Event).filter(Event.id == id).first()

    def create(self, db: Session, data) -> Optional[Event]:
        db_obj = Event(
            **data
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

event_service = EventService()