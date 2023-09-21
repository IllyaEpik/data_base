import json
import os
import customtkinter as ctk
import time
hours = time.localtime()[3]

if 6 < hours < 12:
    color = 'black'
    color2 = 'white'
    screen = ctk.CTk('yellow')
elif 12 < hours < 18:
    color = 'black'
    color2 = 'white'
    screen = ctk.CTk('white')
elif 18 < hours < 24:
    color2 = 'white'
    color = 'black'
    screen = ctk.CTk('orange')
else:
    color = 'white'
    color2 = 'black'
    screen = ctk.CTk('black')
# if 6 < hours < 12:


app_width, app_height = 800, 700
screen.geometry(f"{app_width}x{app_height}+{screen.winfo_screenwidth() // 2 - app_width // 2}+{screen.winfo_screenheight() // 2 - app_height // 2}")
screen.resizable(False, False)

name = ctk.CTkEntry(screen, bg_color = color, fg_color = color, width = 400, height = 100, placeholder_text = 'Enter your name', placeholder_text_color = color2)
name.place(x= 400, y = 100, anchor= ctk.CENTER)

surname = ctk.CTkEntry(screen, bg_color = color, fg_color = color, width = 400, height = 100, placeholder_text = 'Enter your surname', placeholder_text_color = color2)
surname.place(x= 400, y = 250, anchor= ctk.CENTER)

age = ctk.CTkEntry(screen, bg_color = color, fg_color = color, width = 400, height = 100, placeholder_text = 'Enter your age', placeholder_text_color = color2)
age.place(x= 400, y = 400, anchor= ctk.CENTER)

name_json = ctk.CTkEntry(screen, bg_color = color, fg_color = color, width = 200, height = 100, placeholder_text = 'json name', placeholder_text_color = color2)
name_json.place(x= 200, y = 600, anchor= ctk.CENTER)

file1 = __file__.split("/")
del file1[-1]
file1 = "/".join(file1)
def create_dict():
    times = time.localtime()
    data_user = {
        'name': name.get(),
        'surname': surname.get(),
        'age': age.get(),

        "date":times[2],
        "month":times[1],
        "year":times[0],

        'hours':times[3],
        'minutes':times[4],
        'seconds':times[5]

    }
    return [data_user]
def create_floaders(list_name, path):
    for file2 in list_name:
        if file2 != list_name[-1]:
            if file2 != '':
                try:
                    os.mkdir(path + '/' + file2)
                    path += '/' + file2
                except FileExistsError:
                    path += '/' + file2
                except:
                    pass
    return path
def checkError(name_json = None):
    global data_user, file1
    if name.get() != '':
        if surname.get() != '':
            if age.get() != '':
                data_user = create_dict()
                symbol = '\ '
                list_name = name_json.split(":")
                name_json = '-'.join(list_name)

                list_name = name_json.split("*")
                name_json = '-'.join(list_name)

                list_name = name_json.split("?")
                name_json = '-'.join(list_name)

                list_name = name_json.split("<")
                name_json = '-'.join(list_name)

                list_name = name_json.split(">")
                name_json = '-'.join(list_name)

                list_name = name_json.split("|")
                name_json = '-'.join(list_name)

                list_name = name_json.split('''"''')
                name_json = '-'.join(list_name)

                list_name = name_json.split(symbol[0])
                name_json = '/'.join(list_name)
                list_name = name_json.split('/')
                path = ''
                path += file1
                a = ''
                a += list_name[-1] 
                list_name[-1] = None
                path = create_floaders(list_name, path)

                name_json = a
                list_name = name_json.split(".") # ["my_json"]
                if len(list_name) < 2:
                    list_name += ["json"] # ["my_json", "json"]
                    name_json = ".".join(list_name) # "my_json.json"
                elif len(list_name) > 1:
                    list_name[-1] = "json" # ["my_json", "json"]
                    name_json = ".".join(list_name) # "my_json.json"
                try:
                    create_json(file_dict= data_user, name_json= name_json,path = path)
                except:
                    print('error file')


def create_json(file_dict = None, name_json = None, path = file1):
    global file1
    try:
        os.chdir(path)
        with open(name_json, "w") as file:
            json.dump(file_dict, file, indent = 4, ensure_ascii = False)
    except OSError:
        checkError(file_dict=file_dict, name_json= name_json)



button = ctk.CTkButton(screen, text = 'save json', bg_color = color, fg_color = color,text_color = 'yellow',
                        width = 200, height = 100,command = lambda: checkError(name_json.get()))

button.place(x= 600, y = 600, anchor= ctk.CENTER)

data_user = None

screen.mainloop()