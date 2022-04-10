from aiohttp import web
from alembic.config import Config
from sqlalchemy import create_engine, MetaData

from app.routes import setup_routes
from app.settings import config


app = web.Application()
setup_routes(app)
app['config'] = config
web.run_app(app, port=config['common']['port'])