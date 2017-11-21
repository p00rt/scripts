#!/usr/bin/python3
"""
Copyright 2017 Michał Kern

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
# if set to True program won't do anything, just print what it'd do.
DBG = False
import re
from os import listdir, system
from sys import argv

if len(argv) < 2:
    print("Usage: ./renameandtag.py [directory] [album name] [year] [artist name]")
    quit()

directory = argv[1] if len(argv)>1 else "./"
album_name = argv[2] if len(argv)>2 else "Unknown"
year = argv[3] if len(argv)>3 else "Unknown"
artist_name = argv[4] if len(argv)>4 else "Unknown"

# separator (between song number and title)
# has to be escaped, it's injected into regexp
separator = "\-"
regexp = re.compile("(\d\d){}(.*)\.mp3".format(separator))

files = []
for i in listdir(directory):
    if i.find("mp3") != -1:
        files.append(i)

for i in files:
    data = regexp.findall(i)[0]
    if DBG:
        print('id3v2 -t "{}" -A "{}" -a "{}" -T {}/{} "{}"'.format(data[1],
              album_name, artist_name, data[0], len(files), directory + "/" + i))
        print('mv "{}" "{}.mp3"'.format(directory + "/" + i, 
                                    directory + "/" + data[0] + ". "+data[1]))
    else:
        system('id3v2 -t "{}" -A "{}" -a "{}" -T {}/{} "{}"'.format(data[1],
              album_name, artist_name, data[0], len(files), directory + "/" + i))
        system('mv "{}" "{}.mp3"'.format(directory + "/" + i, 
                                    directory + "/" + data[0] + ". "+data[1]))
