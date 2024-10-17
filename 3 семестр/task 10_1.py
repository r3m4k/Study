import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_minor_planets:_1%E2%80%931000'
data = pd.read_html(url)

table = pd.concat((data[i] for i in range(1, 11)), ignore_index=True)

columns_name = ['Permanent', 'Provisional', 'Citation', 'Date', 'Site', 'Discoverer(s)', 'Category', 'Diam.', 'Ref']
table.columns = columns_name

table.drop(['Provisional', 'Category', 'Ref'], axis=1, inplace=True)
print(table)

print('\n\n///////////////////////////////////////////////\n\n')


# ////////////////////

def name_from_str(data_str):
    out = [None, None]
    if ',' in data_str:
        out[0] = data_str[:data_str.find(',')]
        out[1] = data_str[data_str.find(',') + 2:]
    else:
        out[0] = data_str
    return out


def func(data_column):
    df = {}
    for i in range(len(data_column)):
        result = name_from_str(data_column[i])
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


# ////////////////////


scientist = func(table['Discoverer(s)'])
sort_scientist = sorted(scientist.items(), key=lambda x: x[1], reverse=True)

for i in range(3):
    print(sort_scientist[i])

print('\n\n///////////////////////////////////////////////\n\n')

# ////////////////////


def year(data_str):
    return int(data_str[data_str.find(',')+1 : ])


# ////////////////////


years = table['Date'].apply(year)
filter_before_1850_year = years < 1850
print(table[filter_before_1850_year])

filter_1900_1910_year = (years > 1900) & (years < 1910)
print(table[filter_1900_1910_year])

filter_from_1915 = years > 1915
print(table[filter_from_1915])
