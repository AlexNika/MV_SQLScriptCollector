import enum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, text

from mixins import TimestampMixin
from src import db


class DialectEnum(enum.Enum):
    POSTGRESQL = 'postgresql'
    MYSQL = 'mysql'
    MSSQL = 'mssql'
    SQLITE = 'sqlite'
    MONGODB = 'mongodb'
    MARIADB = 'mariadb'


class Script(TimestampMixin, db.Model):

    __tablename__ = 'scripts'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(db.String(length=64), unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(db.String(length=128))
    code: Mapped[text] = mapped_column(Text)
    dialect: Mapped[enum] = mapped_column(db.Enum(DialectEnum), default=DialectEnum.POSTGRESQL, nullable=False)
    author_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=False)
