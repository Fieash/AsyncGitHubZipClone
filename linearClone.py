import urllib.request as ur

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
        counter += 1
        #download file
        request = ur.urlopen(url)
        print("made a request to " + url)
        #save
        output = open("clone2/master"+str(counter)+".zip", "ab")
        output.write(request.read())
        output.close()

main()