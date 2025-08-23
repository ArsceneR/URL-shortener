from flask import Flask
from app.routes.home import home_bp
from app.short_url_generator import URLShortener
from app.pg_database import PostgreDB

def create_app(config_class=None):
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    
    app.config.from_object(config_class) 
    
    app.url_shortener = URLShortener(length=app.config["SHORT_URL_LENGTH"]) #bind url shortener instance  to app
    app.database = PostgreDB(app.config["DB_CONFIG"]) #bind database instance to app

    return app 
