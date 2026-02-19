# import json
# filename = 'students.json'
# with open (filename) as w:
#    students = json.load(w)
import json
with open ("students.json") as f:
    data = json.load(f)
for item in data["student"]:
     print(f"{item['name']}  {item['lastname']}"  f" {item['year']} ")