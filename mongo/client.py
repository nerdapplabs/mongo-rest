import motor
from motor.motor_asyncio import AsyncIOMotorClient
import logging

m_client = motor.motor_asyncio.AsyncIOMotorClient()

db = m_client.m1
collection = db.m1c


async def do_insert(doc):
    result = await collection.insert(doc)
    return result


async def do_find_all():
    async for document in collection.find({}):
        print(document)
        logging.info(document)
    return document


async def do_find_one():
    document = await collection.find_one({})
    print(document)


async def do_count():
    cnt = await collection.find().count()
    print('%s Count of documents ' % cnt)
    return cnt


async def do_del():
    n = await collection.count()
    print('%s Documents before calling del()' % n)
    result = await collection.delete_many({})
    print('%s Documents after!' % (await collection.count()))
    return result


async def do_update():
    result = await collection.update_one({'firstName': 'N', 'lastName': 'M'}, {'$set': {'Position': 'Employee'}})
    print('Updated %s document' % result.modified_count)
    ndoc = await collection.find_one({'firstName': 'N', 'lastName': 'M'})
    print('Document is now %s' % ndoc)
    return ndoc


async def do_replace():
    pass




