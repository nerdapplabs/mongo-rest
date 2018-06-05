#!/usr/bin/env python3

import ujson
from aiohttp.web import Response
from mongo import client as m_client
import logging


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

    # to get all documents in the collection
    if user_id == '0':
        data = await m_client.do_find_all()
        logging.info(data)
        return Response(text=ujson.dumps(data, indent=1), status=200)
    # to get mentioned _id
    else:
        # check if _id exists
        user_data = await m_client.do_find_one(user_id)
        if not user_data:
            logging.error('INVALID _id %s!', user_id)
            return Response(text='Invalid _id !')
        logging.debug('RECORDS: %s', user_data)
        return Response(text=ujson.dumps(user_data), status=200)


async def delete_user(request):
    logging.info('READING THE _id...')
    # user_id_delete_request
    user_id = request.match_info.get('user_id')
    # check if _id exists
    user_data = await m_client.do_find_one(user_id)
    if not user_data:
        logging.error('INVALID _id %s!', user_id)
        return Response(text='Invalid _id !')
    await m_client.do_del(user_data)
    logging.info('DATA DELETED...')
    return Response(text='Deleted !', status=200)


async def update_user(request):
    logging.info('READING THE _id...')
    # user_id_update_request
    user_id = request.match_info.get('user_id')
    user_data = await request.json()
    data = dict(user_data)
    # check if _id exists
    doc = await m_client.do_find_one(user_id)
    if not doc:
        logging.error('INVALID _id %s!', user_id)
        return Response(text='Invalid _id !')
    await m_client.do_update(user_id, data)
    logging.info('DATA UPDATED...')
    return Response(text='Updated !', status=200)


"""
async def count_user(request):
    d = await m_client.do_count()
    return Response(text=json.dumps(d), status=200)
"""
