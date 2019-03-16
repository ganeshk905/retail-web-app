# third-party imports
import os, logging
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import abort, Flask, render_template

logger = logging.getLogger(__name__)
# local imports
db = SQLAlchemy()

from flask_login import LoginManager
login_manager = LoginManager()

from app import models

from config import app_config
def create_app(config_name):
    logger.info("[retaial-web-app] create app")
    logger.info("[retaial-web-app]  input paameters {} {}".format(os.getenv('FLASK_CONFIG'), "production"))
    if os.getenv('FLASK_CONFIG') == "production":
        logger.info("[retaial-web-app] reading environment variable for production")
        app = Flask(__name__)
        app.config.update(SECRET_KEY=os.getenv('SECRET_KEY'),
                          SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI'))
    else:
        logger.info("[retaial-web-app] reading environment variable for production")
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')

    logger.info("[retaial-web-app] initialize Bootstrap")
    Bootstrap(app)
    logger.info("[retaial-web-app] initialize Database")
    db.init_app(app)

    logger.info("[retaial-web-app] initialize Login Manager")
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    logger.info("[retaial-web-app] migrate database")
    migrate = Migrate(app, db)

    logger.info("[retaial-web-app] Register blueprint for each module")
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .inventory import inventory as inventory_blueprint
    app.register_blueprint(inventory_blueprint)

    from .product import product as product_blueprint
    app.register_blueprint(product_blueprint)

    from .customer import customer as customer_blueprint
    app.register_blueprint(customer_blueprint)

    logger.info("[retaial-web-app] Error handlers")
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    @app.route('/500')
    def error():
        abort(500)

    return app
