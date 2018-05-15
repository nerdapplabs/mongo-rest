from aiohttp.web import Response
import json

from mongo import client as m_client


async def handler(request):
    await m_client.do_count()
    mdoc = {'status1': 'success'}
    return Response(text=json.dumps(mdoc), status=200)


async def handle(request):
    await m_client.do_find_all()
    mdoc = {'status2': 'success'}
    return Response(text=json.dumps(mdoc), status=200)


async def update(request):
    await m_client.do_update()
    mdoc = {'status4': 'success'}
    return Response(text=json.dumps(mdoc), status=200)


async def delete(request):
    await m_client.do_del()
    mdoc = {'status3': 'success'}
    return Response(text=json.dumps(mdoc), status=200)


async def new_user(request):
    try:
        doc = {"firstName": "N", "lastName": "M"}
        await m_client.do_insert(doc)
        response_doc = {'status': 'success'}
        return Response(text=json.dumps(response_doc), status=200)

    except Exception as ex:
        response_obj = {'status': 'failed', 'reason': str(ex)}
        return Response(text=json.dumps(response_obj), status=500)
