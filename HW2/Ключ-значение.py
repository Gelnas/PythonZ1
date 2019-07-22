import pprint
d = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    }
new_d = {d[x]: x for x in d.keys()}
pprint.pprint(new_d)
input()
