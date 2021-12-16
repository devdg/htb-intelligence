#!/usr/bin/python3

import urllib.request

urlin = "http://intelligence.htb/documents/"
extension = ".pdf"

day = 1
month = 1
year = 2020
suffix = "-upload"

while month < 13:
        while day < 32:
                file=str(year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2) + suffix + extension
                urltofile = urlin + file
                request = urllib.request.Request(urltofile)
                request.get_method = lambda: 'HEAD'
                try:
                        urllib.request.urlopen(request)
                        print("Downloading:",urltofile)
                        urllib.request.urlretrieve(urltofile,file)
                except urllib.request.HTTPError:
                        print("No file found at:",urltofile)
                day = day + 1
        month = month +1
        day = 1

