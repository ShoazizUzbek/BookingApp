from aiohttp import web

from database.config import session, engine
from service.user import user_service
from validator import UserCreate


async def user_create(request: web.Request):
    user_data = await request.json()
    data_validated = UserCreate(**user_data).dict()
    try:
        user = user_service.create(session, data_validated)
    except Exception as ex:
        return web.json_response(
            {'error': str(ex)},
            status=400
        )
    return web.json_response(
        {'user': user.to_dict()}
    )


async def user_login(request: web.Request):
    user_data = await request.json()
    user = user_service.get_by_name(session, user_data['name'])
    if not user:
        raise web.HTTPForbidden
    return web.json_response(
        {'token': user.to_dict()}
    )

async def all_user_list(request: web.Request):
    users = user_service.all_users(session)
    data = []
    for user in users:
        data.append({
            'id': user.id,
            'name': user.name,
            'surname': user.surname
        })
    return web.json_response(data)


async def user_list(request: web.Request):
    print('f')
    sql = engine.execute('SELECT * FROM user')
    print(sql)
    return web.json_response({'d':'d'})