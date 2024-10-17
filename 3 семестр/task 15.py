import json

data = {'a': [1, 2, 3, 4, 5],
        'n': 3}

file = open('config.json', 'w')
json.dump(data, file)

data1={
        'a': 1,
        'n': [1, 2, 3]
}
file1 = open('config_1.json', 'w')
json.dump(data1, file1)
