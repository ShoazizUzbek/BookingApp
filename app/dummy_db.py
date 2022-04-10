# from sqlalchemy import (Table, Column, ForeignKey,
#                         Integer, String, Date)
# from sqlalchemy.ext.declarative import declarative_base
#
# from app.settings import metadata
#
#
# user = Table(
#     'user', metadata,
#
#     Column('id', Integer, primary_key=True),
#     Column('name', String(155), unique=True, nullable=False),
#     Column('surname', String(155), nullable=False),
#     Column('token', String(255), nullable=False, unique=True,),
# )
#
# event = Table(
#     'event', metadata,
#
#     Column('id', Integer, primary_key=True,),
#     Column('remain', Integer, nullable=False,),
#     Column('title', String(155), nullable=False,),
#     Column('description', String(255), nullable=False,),
#     Column('price', Integer, nullable=False,),
#     Column('date', Date, nullable=False,),
# )
#
# coupon = Table(
#     'coupon', metadata,
#
#     Column('id', Integer, primary_key=True,),
#     Column('event_id',
#            ForeignKey('event.id', ondelete='CASCADE'),
#            ),
#     Column('user_id',
#            ForeignKey('user.id', ondelete='CASCADE'),
#            ),
#     Column('hash', String(255), nullable=False, unique=True,),
# )