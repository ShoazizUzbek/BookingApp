import re
from typing import Tuple, Callable

from aiohttp import web


def is_exclude(request, exclude):
    for pattern in exclude:
        if re.fullmatch(pattern, request.path):
            return True
    return False


def token_auth_middleware(
    user_loader: Callable,
    request_property: str = "user",
    exclude_routes: Tuple = tuple(),
    exclude_methods: Tuple = tuple(),
):
    @web.middleware
    async def middleware(request, handler):
        if is_exclude(request, exclude_routes) or request.method in exclude_methods:
            return await handler(request)
        try:
            token = request.headers["Authorization"]
        except KeyError:
            raise web.HTTPUnauthorized(
                reason="Missing authorization header",
            )
        except ValueError:
            raise web.HTTPForbidden(
                reason="Invalid authorization header",
            )

        user = await user_loader(token)

        if user:
            request[request_property] = user
        else:
            raise web.HTTPForbidden(reason="Token doesn't exist")

        return await handler(request)

    return middleware
