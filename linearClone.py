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

def main():
    counter = 0
    URLList = readfile("5Sites.txt")
    for url in URLList:
        filename = url.split("/")
        filename = filename[4]
        counter += 1
        #download file
        request = ur.urlopen(url)
        print("made a request to " + url)
        #save
        output = open("clone1/"+filename+".zip", "ab")
        output.write(request.read())
        output.close()
