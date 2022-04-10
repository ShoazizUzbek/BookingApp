from sqlalchemy import Column, Integer, String, Date, ForeignKey

from app.database.config import Base


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True,)
    name = Column(String(155), unique=True, nullable=False,)
    surname = Column(String(155), unique=True, nullable=False,)
    token = Column(String(255), unique=True, nullable=False,)

    @classmethod
    async def get_user_by_name(cls, name):
        return await User.query.where(User.username == name).gino.first()

    @classmethod
    async def get_user_by_token(cls, token):
        return await User.query.filter_by(User.token == token).first()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'token': self.token
        }


class Event(Base):

    __tablename__ = 'event'

    id = Column(Integer, primary_key=True,)
    remain = Column(Integer, nullable=False,)
    title = Column(String(155), nullable=False,)
    description = Column(String(255), nullable=False,)
    price = Column(Integer, nullable=False,)
    date = Column(Date, nullable=False,)


class Coupon(Base):

    __tablename__ = 'coupon'

    id = Column(Integer, primary_key=True,)
    event_id = Column(ForeignKey('event.id', ondelete='CASCADE'), nullable=False,)
    user_id = Column(ForeignKey('user.id', ondelete='CASCADE'), nullable=False,)
    hash = Column(String(25), unique=True, nullable=False,)