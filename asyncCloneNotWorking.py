import urllib.request as ur
import asyncio
import time

def readfile(filename):
    cloneURLList = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            line += "/archive/master.zip"
            cloneURLList.append(line)
    return cloneURLList

async def clone(url):
    filename = url.split("/")
    filename = filename[-3]
    #download file
    request = ur.urlopen(url)
    print("made a request to " + url)
    #save
    output = open("clone1/"+filename+".zip", "ab")
    output.write(request.read())
    output.close()
    await asyncio.sleep(0.01)

if __name__ == "__main__":
    t0 = time.time()

    loop = asyncio.get_event_loop()
    URLList = readfile("5Sites.txt")
    tasks = [asyncio.ensure_future(clone(u))for u in URLList]
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    t1 = time.time()
    print('Time taken %.2f seconds' % (t1-t0))