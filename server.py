#!/usr/bin/env python3

from aiohttp import web
from api import api


def run():
    """ Starts the Server """

    app = web.Application()
    app.router.add_get('/api/ping', api.ping)
    web.run_app(app)

import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
run()