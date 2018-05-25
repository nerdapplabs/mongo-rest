import ujson

from aiohttp.web import Response

from mongo import client as m_client

import logging.config

import json

from os import path, remove

if path.isfile("logging_config.log"):
    remove("logging_config.log")

with open("app.json", 'r') as f:
    config_dict = json.load(f)
logging.config.dictConfig(config_dict)
logger = logging.getLogger(__name__)
logger.info("Logging!")


async def add_user(request):
    logging.info('READING THE DATA...')
    # user_id_insert_request
    user_data = await request.json()
    user_id = user_data.get("_id")
    # check if _id already exists
    check_id = await m_client.do_find_one(user_id)
    if not check_id:
        logging.info('ADDING RECORDS...')
        inserted_data = await m_client.do_insert(user_data)
        logging.info('INSERTED DATA...')
        # find the inserted_data
        find_data = await m_client.do_find_one(inserted_data)
        logging.debug('RECORDS: %s', find_data)
        return Response(text=ujson.dumps(find_data), status=200)
    logging.error('_ID ALREADY EXISTS...')
    return Response(text='_id already exists !')


async def get_user(request):
    logging.info('READING THE _id...')
    #  user_id_find_request
    user_id = request.match_info.get('user_id')
    # check if _id exists
    user_data = await m_client.do_find_one(user_id)
    if not user_data:
        logging.error('INVALID _id %s !', user_id)
        return Response(text='Invalid _id !')
    logging.debug('RECORDS: %s', user_data)
    return Response(text=ujson.dumps(user_data), status=200)


async def delete_user(request):
    logging.info('READING DATA...')
    # user_id_delete_request
    user_id = request.match_info.get('user_id')
    # check if _id exists
    user_data = await m_client.do_find_one(user_id)
    if not user_data:
        logging.error('INVALID _id %s !', user_id)
        return Response(text='Invalid _id !')
    await m_client.do_del(user_data)
    logging.info('DATA DELETED...')
    return Response(text='Deleted !', status=200)


# Not complete !
async def update_user(request):
    # user_id_update_request
    user_id = request.match_info.get('user_id')
    user_data = await request.ujson()
    data = dict(user_data)
    print(data)
    doc = await m_client.do_find_one(user_id)
    doc_data = doc.get('f_name', 'l_name')
    print(doc_data)
    if not doc:
        return Response(text='Invalid _id !')
    '''if f_name is None:
        f_name = doc.get("f_name")
        await m_client.do_update(user_id, f_name, l_name)
    elif l_name is None:
        l_name = doc.get("l_name")
        await m_client.do_update(user_id, f_name, l_name)
    else:'''
    await m_client.do_update(user_id, data)
    return Response(text='Updated !', status=200)


"""
async def count_user(request):
    d = await m_client.do_count()
    return Response(text=json.dumps(d), status=200)
"""
