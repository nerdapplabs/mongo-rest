import json

from aiohttp.web import Response

from mongo import client as m_client


async def handler(request):
    request = await m_client.do_count()
    mdoc = {'status1': 'success'}
    return Response(text=json.dumps(mdoc), status=200)


async def get_user(user_id=None):
    d = await user_id.json()
    print(d)
    await m_client.do_find_one(d)
    response_doc = {'status2': 'success'}
    return Response(text=json.dumps(response_doc), status=200)


async def update_user(user_data):
    d = await user_data.json()
    print(d)
    await m_client.do_update(d)
    response_doc = {'status4': 'success'}
    return Response(text=json.dumps(response_doc), status=200)


async def delete_user(user_id):
    d = await user_id.json()
    await m_client.do_del(d)
    response_doc = {'status3': 'success'}
    return Response(text=json.dumps(response_doc), status=200)


async def add_user(user_data):
    d = await user_data.json()
    print(d)
    await m_client.do_insert(d)
    response_doc = {'status': 'success'}
    return Response(text=json.dumps(response_doc), status=200)

