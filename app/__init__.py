from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import config_options
from flask_uploads import UploadSet, IMAGES, configure_uploads

# from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
mail = Mail()
photos = UploadSet('photos', IMAGES)

login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    # initialize
    db.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    # Regestering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Regestering the auth bluprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    configure_uploads(app,photos)

    return app