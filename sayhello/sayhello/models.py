
from datetime import datetime

from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

# from sqlalchemy import Integer, String, DateTime
# from sqlalchemy.orm import Mapped, mapped_column

# class Message(db.Model):
#     id: Mapped[Integer] = mapped_column(primary_key=True)
#     name: Mapped[String(20)] = mapped_column()
#     body: Mapped[String(200)] = mapped_column()
#     timestamp: Mapped[DateTime] = mapped_column(default=datetime.utcnow, index=True)