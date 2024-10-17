#Вариант 2
#Делал этот вариант, потому что ссылка на 1-ый вариант не читается PyCharm-ом, и он выдаёт ошибку

import numpy as np
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_chemical_elements'
data = pd.read_html(url)

table = data[0]
#print(table.head())

columns_name = ['Atomic number. Z', 'Symbol', 'Name', 'Origin of name', 'Group', 'Period', 'Block',
                'Standard atomic weight Ar°(E)', 'Density', 'Melting points', ' Boiling points',
                'Specific heat capacity', 'Electronegativity', "Abundance in Earth's crust",
                'Origin', 'Phase at r.t.']

table.columns = columns_name
table.drop(axis=0, inplace=True, index=0)
table.drop(['Origin of name', 'Origin', 'Block'], axis=1, inplace=True)

print(table.head())

# Sort

def Pc_to_number(data_str):
    out = None
    if '(' not in data_str:
        out = data_str
        out = float(out)

    if '(' in data_str:
        out = data_str[data_str.find('(')+1 : data_str.find('±', '–', ')')]
    return out


Pc = table['Density']
Pc.apply(Pc_to_number)


#table_sort = table.sort_values(by='Density')
#print(table_sort.head())

'''
# Gases, solid, liguid

print(table.head())

table_gas = table[table['Phase at r.t.'] == 'gas']
print(table_gas.head())

table_solid = table[table['Phase at r.t.'] == 'solid']
print(table_solid.head())

table_liquid = table[table['Phase at r.t.'] == 'liquid']
print(table_liquid.head())
'''
