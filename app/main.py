from aiohttp import web
from alembic.config import Config
from sqlalchemy import create_engine, MetaData

from app.database.config import session
from app.middleware import token_auth_middleware
from app.routes import setup_routes
from app.service.user import user_service
from app.settings import config

async def user_loader(token: str):
    user = user_service.get_by_token(session,token)
    if user:
        return user
    else:
        return None


app = web.Application(middlewares=[token_auth_middleware(
    user_loader=user_loader,
    exclude_routes=('/user/create', '/user/login')
)])
setup_routes(app)
app['config'] = config
web.run_app(app, port=config['common']['port'])