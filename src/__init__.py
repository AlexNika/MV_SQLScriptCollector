from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from config import Config


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    })


app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')
app.config.from_object(Config)
db = SQLAlchemy(model_class=Base)
# db.init_app(app)
migrate = Migrate(app, db)

from src.core.views import core_bp
from .users.views import users_bp
from src.scripts.views import scripts_bp
from .contacts.views import contacts_bp

app.register_blueprint(core_bp)
app.register_blueprint(users_bp)
app.register_blueprint(scripts_bp)
app.register_blueprint(contacts_bp)
