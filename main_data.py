
import sqlite3
import os
# Find absolute path of the folder work_data_base
path = os.path.abspath(__file__ + '/../data_base')
#
print(f"\n\t{path}\n")
# Set general dirictory for save files  
try:
    os.chdir(path)
except FileNotFoundError:
    os.mkdir(path)
    os.chdir(path)
# Create database "newDataBase10.db" 
data_base = sqlite3.connect('newDataBase10.db')
#
pen = data_base.cursor()
#
# create_table = "CREATE TABLE IF NOT EXISTS Users (ID INTEGER PRIMARY KEY, name TEXT, surname TEXT,)"
#
def create_table(name_table = '', list_values = tuple(('name_colum', 'type_value'))):
    table = f'CREATE TABLE IF NOT EXISTS {name_table} (' 
    count = 0
    for tuple in list_values:
        if count < len(list_values) - 1:
            table = f"{table} {tuple[0]} {tuple[1]}, "
        else: 
            table = f'{table} {tuple[0]} {tuple[1]})'
        count += 1
    # table += ')'
    return  table 
#
pen.execute(
    create_table(
        name_table= "Trees", 
        list_values= (
                        ("id", 'INTEGER PRIMARY KEY'), ('name', 'TEXT'), ('surname', 'TEXT'), ('age', 'INTEGER')
                    )
                )
)
# save data in database
data_base.commit()
# close file database
data_base.close() 