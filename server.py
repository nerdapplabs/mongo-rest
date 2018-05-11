from aiohttp import web
from api import handler


def run():
    """ Starts the Server
    """
    app = web.Application()
    app.router.add_get('/', handler.handler)
    app.router.add_post('/insert', handler.new_user)
    app.router.add_get('/find', handler.handle)
    app.router.add_patch('/update', handler.update)
    app.router.add_delete('/delete', handler.delete)
    web.run_app(app)


run()
