from dotenv import load_dotenv
import os

load_dotenv()


DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')


REDIS_HOST_P = os.environ.get('REDIS_HOST_P')
REDIS_USER_P = os.environ.get('REDIS_USER_P')
REDIS_PASS_P = os.environ.get('REDIS_PASS_P')
REDIS_PORT_P = os.environ.get('REDIS_PORT_P')

REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_HOST = os.environ.get('REDIS_HOST')

BROKER_URL = os.environ.get('BROKER_URL')


