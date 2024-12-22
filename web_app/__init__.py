from flask import Flask
import os
import yaml
from logger import CustomLogger
from dotenv import load_dotenv
load_dotenv()

class AppConfig:
    def __init__(self):
        self.config = self.load_config()
    
    def load_config(self):
        with open('config/config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        if 'api' in config and 'key' in config['api']:
            config['api']['key'] = os.getenv('API_KEY')
        return config

def create_app():
    app = Flask(__name__, template_folder='templates')
    app_config = AppConfig()
    app.config.update(app_config.config)
    logger = CustomLogger().get_logger()
    logger.info("Flask application starting...")
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app