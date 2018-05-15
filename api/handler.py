import json

from aiohttp.web import Response, post

from mongo import client as m_client


async def handler(request):
    await m_client.do_count()
    mdoc = {'status1': 'success'}
    return Response(text=json.dumps(mdoc), status=200)


async def handle(request):
    d = await request.json()
    await m_client.do_find_one(d)
    mdoc = {'status2': 'success'}
    return Response(text=json.dumps(mdoc), status=200)


async def update(request):
    d = await request.json()
    print(d)
    await m_client.do_update(d)
    response_doc = {'status4': 'success'}
    return Response(text=json.dumps(response_doc), status=200)


async def delete(request):
    await m_client.do_del()
    mdoc = {'status3': 'success'}
    return Response(text=json.dumps(mdoc), status=200)


async def new_user(request):
    d = await request.json()
    print(d)
    await m_client.do_insert(d)
    response_doc = {'status': 'success'}
    return Response(text=json.dumps(response_doc), status=200)

