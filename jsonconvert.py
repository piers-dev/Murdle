import json


import json
text = open('words.txt','r').read().splitlines()
f = open('f.txt','x')
newf = json.dumps(text)
f.write(newf)
f.close()