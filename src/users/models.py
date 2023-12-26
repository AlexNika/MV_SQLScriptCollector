from datetime import datetime

from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column

from mixins import TimestampMixin
from src import bcrypt, db


class User(TimestampMixin, UserMixin, db.Model):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(db.String)
    user_id: Mapped[int] = mapped_column(db.Integer, unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String, unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String, nullable=False)
    is_admin: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)

    def __init__(self, name, user_id, email, password, is_admin=False):
        self.name = name
        self.user_id = user_id
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<email {self.email}>"
