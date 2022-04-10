from aiohttp import web

from app.database.config import  session
from app.service.event import event_service
from app.validator import EventData


async def event_create(request: web.Request):
    data = await request.json()
    data_validated = EventData(**data).dict()
    try:
        event = event_service.create(session, data_validated)
    except Exception as ex:
        return web.json_response(
            {'error': str(ex)},
            status=400
        )
    return web.json_response(
        {'event': event.to_dict()}
    )


async def event_list(request: web.Request):
    users = event_service.all_events(session)
    data = []
    for user in users:
        data.append(
            user.to_dict()
        )
    return web.json_response(data)
