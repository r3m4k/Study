def name_from_str(data_str):
    out = [None, None]
    if ',' in data_str:
        out[0] = data_str[:data_str.find(',')]
        out[1] = data_str[data_str.find(',')+2:]
    else:
        out[0] = data_str
    return out

def func(data_str):
    df = {}
    result = name_from_str(data_str)
    if result[0] in df:
        df[result[0]] += 1
    else:
        df[result[0]] = 1

    if result[1]:
        if result[1] in df:
            df[result[1]] += 1
        else:
            df[result[1]] = 1

    return df

df1 = func(input('Start\n')
print(df1)

print()
