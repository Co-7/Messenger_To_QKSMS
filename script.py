import json
import sys

#Variable Form
jsonFile = sys.argv[1]
me = sys.argv[2]
numberContact = sys.argv[3]

# Opening JSON file
f = open(jsonFile, "r")

# returns JSON object as
data = json.load(f)

# Changes the Json File
for i in data['messages']:
    i["locked"] = False
    i["status"] = -1
    i["protocol"] = 0
    i["read"] = True
    i["address"] = numberContact
    i["date"] = i["timestamp_ms"]
    if i["sender_name"] == me:
        i["type"] = 2
        i["subId"] = -1
        i["dateSent"] = i["date"]
    else:
        i["type"] = 1
        i["subId"] = 1
        i["dateSent"] = 0
    i.pop('sender_name', None)
    i.pop('timestamp_ms', None)
    i.pop('share', None)
    i.pop('reactions', None)
    try:
        content = i["content"]
        content = content.encode('latin1').decode('utf8')
        i["body"] = content
        i.pop('content', None)
    except:
        i.pop('photos', None)

data['messageCount'] = len(data['messages'])
try:
    del data['participants']
except:
    print("")
try:
    del data['title']
except:
    print("")
try:
    del data['is_still_participant']
except:
    print("")
try:
    del data['thread_type']
except:
    print("")
try:
    del data['thread_path']
except:
    print("")

# Writes the New Json file
f = open(jsonFile, 'w', encoding="utf-8")
json.dump(data, f , ensure_ascii = False)

