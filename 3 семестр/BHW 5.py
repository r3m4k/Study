import json
import pickle
import os.path


def function(file_directory):
    file = open(f'{file_directory}', 'r')
    name_pkl_file = 'pkl_file'
    flag = os.path.isfile(name_pkl_file)

    if flag:
        pkl_file = open('pkl_file', 'rb')
        result = pickle.load(pkl_file)
    else:
        result = dict()

    symbol = file.read(1)
    while symbol:
        if symbol in result:
            result[symbol] += 1
        else:
            result[symbol] = 1
        symbol = file.read(1)

    if flag:
        pkl_file.close()

    pkl_file = open(f'{name_pkl_file}', 'wb')
    pickle.dump(result, pkl_file)

    print(json.dumps(result, indent=4))

    pkl_file.close()
    file.close()


function("D:\\Учёба\Инфа\\3 семестр\\Henry Lion Oldie. Master.txt")
