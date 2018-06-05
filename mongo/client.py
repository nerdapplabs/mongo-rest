#!/usr/bin/env python3

import motor
from motor.motor_asyncio import AsyncIOMotorClient
m_client = motor.motor_asyncio.AsyncIOMotorClient()

db = m_client.m1
collection = db.m1c


async def do_insert(user_data):
    document = await collection.insert(user_data)
    return document


async def do_find_one(user_id):
    document = await collection.find_one(user_id)
    return document


async def do_del(user_id):
    await collection.delete_one(user_id)


async def do_update(user_id, user_data):
    await collection.update({"_id": user_id}, {'$set': user_data})


async def do_find_all():
    doc = collection.find()
    return doc


"""
async def do_count():
    cnt = await collection.find().count()
    print('%s Count of documents ' % cnt)
    return cnt
"""
