from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')
app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src.core.views import core_bp
from src.users.views import users_bp
from src.scripts.views import scripts_bp
from src.contacts.views import contacts_bp

app.register_blueprint(core_bp)
app.register_blueprint(users_bp)
app.register_blueprint(scripts_bp)
app.register_blueprint(contacts_bp)

from src.users.models import User

login_manager.login_view = "users.login"
login_manager.login_message_category = "danger"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
