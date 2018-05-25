#!/usr/bin/env python3

from aiohttp import web

from api import handler


def run():
    """ Starts the Server """

    app = web.Application()

    app.router.add_get('/api/user/{user_id}', handler.get_user)
    app.router.add_post('/api/user', handler.add_user)
    app.router.add_put('/api/user/{user_id}', handler.update_user)
    app.router.add_delete('/api/user/{user_id}', handler.delete_user)

    web.run_app(app)


run()


