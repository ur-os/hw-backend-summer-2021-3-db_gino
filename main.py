import os

from app.web.app import setup_app
from aiohttp.web import run_app

FILE_PATH = ''

if __name__ == "__main__":
    run_app(setup_app(config_path=os.path.join(os.path.abspath(__file__), 'config.yml')))
