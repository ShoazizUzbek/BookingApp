from aiohttp import web

from database.config import session
from service.coupon import coupon_service
from validator import CouponData


async def create_coupon(request: web.Request):
    data = await request.json()
    data_validated = CouponData(**data).dict()
    user = request['user']
    coupon = coupon_service.create(session, data_validated['event_id'], user.id)
    return web.json_response(
        {'coupon': coupon.hash}
    )