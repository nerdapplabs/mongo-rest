import motor
from motor.motor_asyncio import AsyncIOMotorClient

m_client = motor.motor_asyncio.AsyncIOMotorClient()

db = m_client.m1
collection = db.m1c


async def do_insert(doc):
    result = await collection.insert(doc)
    return result


async def do_find_one(d):
    document = await collection.find_one(d)
    print(document)


async def do_count():
    cnt = await collection.find().count()
    print('%s Count of documents ' % cnt)
    return cnt


async def do_del(d):
    n = await collection.count()
    print('%s Documents before calling del()' % n)
    result = await collection.delete_one(d)
    print('%s Documents after!' % (await collection.count()))
    return result


async def do_update(d):
    id = await collection.find_one()
    print(id)
    result = await collection.update_one({"_id": 1}, {'$set': d})
    print(result)
    return result





