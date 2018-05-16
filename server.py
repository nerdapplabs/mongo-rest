#!/usr/bin/env python3

from aiohttp import web
from api import handler


def run():
    """ Starts the Server """

    app = web.Application()
    app.router.add_get('/user', handler.handler)
    app.router.add_post('/add/user', handler.add_user)
    app.router.add_get('/find/user', handler.get_user)
    app.router.add_put('/update/user', handler.update_user)
    app.router.add_delete('/delete/user', handler.delete_user)

    web.run_app(app)


run()
