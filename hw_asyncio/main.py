from aiohttp import ClientSession
import asyncio
from datetime import datetime
from model import People, Session, engine, Base
from pprint import pprint


async def post_to_db(people_list):
    async with Session() as session:
        peoples = [People(**people) for people in people_list if 'name' in people]
        session.add_all(peoples)
        await session.commit()


async def get_corutin(people_id: int, client: ClientSession):
    url = f'https://swapi.dev/api/people/{people_id}'
    response = await client.get(url)
    json_data = await response.json()
    return json_data


async def get_people():
    async with ClientSession() as client:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        for list_id in range(1, 92, 10):
            coros = []
            for people_id in range(list_id, list_id+10):
                corutin = get_corutin(people_id, client)
                coros.append(corutin)
            people_list = await asyncio.gather(*coros)
            # pprint(people_list)
            await post_to_db(people_list)

start = datetime.now()
asyncio.run(get_people())
print(datetime.now() - start)

