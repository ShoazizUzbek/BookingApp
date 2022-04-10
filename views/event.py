from aiohttp import web
from sqlalchemy import text

from database.config import session
from service.event import event_service
from config.validator import EventData, EventFilter


async def event_create(request: web.Request):
    data = await request.json()
    data_validated = EventData(**data).dict()
    try:
        event = event_service.create(session, data_validated)
    except Exception as ex:
        return web.json_response({"error": str(ex)}, status=400)
    return web.json_response({"event": event.to_dict()})


async def all_event_list(request: web.Request):
    users = event_service.all_events(session)
    data = []
    for user in users:
        data.append(user.to_dict())
    return web.json_response(data)


async def event_list_by_filter(request: web.Request):
    """
    Event list which filters by persons count and accepted coupons.
    """
    data = await request.json()
    data_validated = EventFilter(**data).dict()
    start = data_validated["start"]
    end = data_validated["end"]
    sql = text(
        f"""SELECT 
                e.id,
                e.title,
                u.name,
                c.hash
            FROM "event" e
            INNER JOIN coupon c on c.event_id=e.id
            INNER JOIN "user" u on u.id=c.user_id
            WHERE e.id IN (
                SELECT id FROM "event" e1
                WHERE (SELECT count(1) FROM coupon WHERE event_id=e1.id) BETWEEN {start} AND {end}
            )"""
    )
    events = session.execute(sql)
    resultset = []
    for row in events:
        resultset.append(dict(row))
    return web.json_response(resultset)
