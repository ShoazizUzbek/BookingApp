from aiohttp import web

from database.config import session
from middleware import token_auth_middleware
from routes import setup_routes
from service.user import user_service
from settings import port


async def user_loader(token: str):
    user = user_service.get_by_token(session,token)
    if user:
        return user
    else:
        return None


application = web.Application(
    # middlewares=[token_auth_middleware(
    # user_loader=user_loader,
    # exclude_routes=('/user/create', '/user/login','/user/list')
# )]
)
setup_routes(application)
web.run_app(application, port=port)