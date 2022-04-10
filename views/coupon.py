from aiohttp import web

from database.config import session
from service.coupon import coupon_service
from config.validator import CouponData


async def create_coupon(request: web.Request):
    data = await request.json()
    data_validated = CouponData(**data).dict()
    user = request["user"]
    try:
        coupon = coupon_service.create(session, data_validated["event_id"], user.id)
    except Exception:
        session.close()
        return web.json_response({"error": "Duplicated enrolling event"}, status=400)
    return web.json_response({"coupon": coupon.hash})
