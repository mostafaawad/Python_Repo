import os, glob, io, json

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

files = []

os.chdir("mp3/")
for file in glob.glob("*.mp3"):
    files.append(file[0:32])

jsonData = {"externalId" : files}

os.chdir("..")

with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(jsonData,indent=4,sort_keys=True,separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
print str_