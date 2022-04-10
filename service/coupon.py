import uuid

from sqlalchemy.orm import Session

from database.models import Coupon


class EventService():

    def user_events(self, db: Session, user_id: int):
        return db.query(Coupon).filter(Coupon.user_id == user_id)

    def create(self, db: Session, event_id, user_id):
        coupon_code = (uuid.uuid4().hex)[:7]
        db_obj = Coupon(
            event_id=event_id,
            user_id=user_id,
            hash=coupon_code,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

coupon_service = EventService()