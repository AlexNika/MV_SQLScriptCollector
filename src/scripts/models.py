from flask_login import current_user

from mixins import TimestampMixin
from src import db


class Script(TimestampMixin, db.Model):

    __tablename__ = "scripts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    name = db.Column(db.String(length=64), unique=True, index=True, nullable=False)
    description = db.Column(db.String(length=128))
    code = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.ForeignKey("users.id"), nullable=False, default=current_user)
    user = db.relationship("User", back_populates="scripts", lazy="select")

    def __init__(self, name, description, code, user_id=current_user):
        self.name = name
        self.description = description
        self.code = code
        self.user_id = user_id

    def __repr__(self):
        return f"<Script {self.email}>"

# TODO реализовать обновление поля scripts_quantity, после добавления нового скрипта
# @db.event.listens_for(Script, "after_insert")
# def after_insert(mapper, connection, target):
