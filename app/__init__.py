from flask import Flask
from flask_sqlalchemy import SQLALchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLALchemy()

migrate = Migrate()

def create_app():
    app = Flask (__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)


    #BLUEPRINTS
    from app.blueprints.public import public_bp
    from app.blueprints.auth import auth_bp
    from app.blueprints.admin import admin_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(auth_bp, url_prefix='/admin')

    return app