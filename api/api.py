import json
from aiohttp.web import Response
import time

_start_time = time.time()


async def ping(request):
    since_started = time.time() - _start_time
    jdoc = {'uptime': since_started}
    return Response(text=json.dumps(jdoc), status=200)