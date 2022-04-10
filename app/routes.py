from app.views.user import user_create, user_login, user_list


def setup_routes(app):
    app.router.add_post('/user/create', user_create)
    app.router.add_post('/user/login', user_login)
    app.router.add_get('/user/list', user_list)