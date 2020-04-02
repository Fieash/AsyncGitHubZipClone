#!/usr/local/bin/python
import asyncio
from aiohttp import ClientSession
import urllib.request as ur
import time

def readfile(filename):
    cloneURLList = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            line += "/archive/master.zip"
            cloneURLList.append(line)
    return cloneURLList

def download_zip(filename, response_read):
    output = open("clone1/"+filename+".zip", "ab")
    output.write(response_read)
    output.close()

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()

async def run(URLList):
    tasks = []
    urlNames = []

    async with ClientSession() as session:
        for url in URLList:
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)
            urlNames.append(url)
            #print("made a request to " + url)


        responses = await asyncio.gather(*tasks)

    for i in range(len(responses)):
        filename = urlNames[i].split("/")
        filename = filename[-3]
        download_zip(filename, responses[i])

t0 = time.time()

URLList = readfile("5Sites.txt")
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(URLList))
loop.run_until_complete(future)

t1= time.time()
print("Projects downloaded: ")
for url in URLList:
    filename = url.split("/")
    filename = filename[-3]
    print(filename)
print('Time taken %.2f seconds' % (t1-t0))
