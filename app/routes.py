from app.views.coupon import create_coupon
from app.views.event import event_create, event_list
from app.views.user import user_create, user_login, all_user_list


def setup_routes(app):
    # user endpoints
    app.router.add_post('/user/create', user_create)
    app.router.add_post('/user/login', user_login)
    app.router.add_get('/all-user/list', all_user_list)
    app.router.add_get('/user/list/', all_user_list) #person list which participated at least in 3 events

    app.router.add_post('/event/create', event_create)
    app.router.add_get('/event/list', event_list)

    app.router.add_post('/coupon/create', create_coupon)
