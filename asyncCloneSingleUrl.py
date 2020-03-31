import signal
import sys
import asyncio
import aiohttp
import json

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)
URL1 = "https://github.com/python/cpython/archive/master.zip"

async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()

async def get_reddit_top(url, client):
    data1 = await get_json(client, url)

    print('DONE WITH URL '+ url)

def signal_handler(signal, frame):
    print("signal handler called")
    loop.stop()
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

asyncio.ensure_future(get_reddit_top(URL1, client))
loop.run_forever()