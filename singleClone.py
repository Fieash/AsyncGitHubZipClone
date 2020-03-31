import urllib.request as ur
import re
import zipfile

#download file
download = "https://github.com/python/cpython/archive/master.zip"
request = ur.urlopen(download)

#save
output = open("master.zip", "wb")
output.write(request.read())
output.close()