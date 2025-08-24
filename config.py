
import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    DOMAIN_NAME = 'example.com'
    DEBUG = False
    
    
class DevConfig(Config):
    DEBUG = True
    DOMAIN_NAME = os.environ.get('DOMAIN_NAME', 'localhost') + ':'+ os.environ.get('PORT', '8000')
    PORT = int(os.environ.get('PORT', 8000))
    PROTOCOL = os.environ.get('PROTOCOL', 'http')
    SHORT_URL_LENGTH = int(os.environ.get('SHORT_URL_LENGTH', 10))
    DB_CONFIG = {
        'database': os.environ['DATABASE'],
        'user': os.environ['USER'],
        'password': os.environ['PASSWORD'],
        'host': os.environ['HOST'],
        'port': os.environ['DB_PORT'],
    }