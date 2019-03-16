import os
import logging
from app import create_app
logger = logging.getLogger(__name__)
config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    logger.info("[retaial-web-app] Running flask app")
    app.run()
