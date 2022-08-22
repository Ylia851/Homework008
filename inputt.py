import outputt
import sqlite3

def User_Data():
    print("Введите ФИО сотрудника: ")
    FIO = input()
    print("Введите дату рождения: ")
    age = input()
    print("Введите страховой номер: ")
    str_number = input()
    print("Введите контактный телефон: ")
    phone = input()
    print("Выберите должность: ")
    post = outputt.Print_Data(post)
    #post = open('post.json', 'r')?
    print('Выберите отдел: ')
    otdel = outputt.Print_Data(otdel)
    return [FIO, age, str_number, phone, post, otdel]

dist1 = {}

def Unput_post():
    print('Введите порядковый номер должности')
    id_post = int(input())
    print('Введите наименование должности: ')
    post = input()
    return [id_post, post]

def Unput_otd():
    print('Введите порядковый номер отдела')
    id_otd = int(input())
    print('Введите наименование отдела: ')
    otdel = input()
    return [id_otd, otdel]

def New_Dist(dist1, data):
    if len(dist1) == 0: id == 1
    else: id = max(dist1.keys())+1
    dist1[id] = data

FIO = New_Dist(dist1, User_Data)
FIO = New_Dist(dist1, User_Data)
Otdel = New_Dist(dist1, Unput_otd)
Otdel = New_Dist(dist1, Unput_otd)
Post = New_Dist(dist1, Unput_post)
Post = New_Dist(dist1, Unput_post)

def Control():
    con = sqlite3.connect("test.db")
    cur = con.cursor
    with con:
        cur.execute("""
        CREATE TABLE user_post (
            id INT,
            post_id INT,
            otdel_id INT)
            PRIMARY KEY(id, post_id, otdel_id,
            FOREIGN KEY(id) REFERENCES user(id),
            FOREIGN KEY(post_id, otdel_id) REFERENCES post(id) REFERENCES otdel(id)
               );
    """)


