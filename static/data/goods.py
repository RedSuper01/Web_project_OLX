import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Goods(SqlAlchemyBase):
    __tablename__ = 'goods'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    good = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date_of_public = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_sold = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    seller = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    photo = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    contacts = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user = orm.relation('User')

    def __repr__(self):
        return f'<Goods> {self.good}'