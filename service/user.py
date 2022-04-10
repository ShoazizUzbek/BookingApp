from typing import Optional

from sqlalchemy.orm import Session

from database.models import User
from security import generate_token



class UserService():

    def all_users(self, db):
        return db.query(User).all()

    def user_events(self, db):
        return db.engine(User).filter()

    def get_by_id(self, db, id: int) -> Optional[User]:
        return db.query(User).filter(User.id == id).first()

    def get_by_token(self, db, token: str) -> Optional[User]:
        return db.query(User).filter(User.token == token).first()

    def get_by_name(self, db, name: str) -> Optional[User]:
        return db.query(User).filter(User.name == name).first()

    def create(self, db, data) -> Optional[User]:
        token = generate_token(data['name']+data['surname'])
        data['token'] = token
        db_obj = User(
            **data
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

user_service = UserService()