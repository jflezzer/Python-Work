import json

input = '''
[
{ "id" : "001",
"x" : "2",
"name" : "Jim"
},
{ "id" : "009",
"x" : "7",
"name" : "Karen"
}
]'''

info = json.loads(input)
print 'User Count:', len(info)

for item in info:
    print 'Name:', item['name']
    print 'Id:', item['id']
    print 'Attribute:', item['x']