import inputt

n = inputt.New_Dist(inputt.dist1, inputt.User_Data)

def Del():
    print('Введите ФИО сотрудника, которого вы хотите удалить')
    element = input()
    for i in n:
        if n[i]['FIO'] == element:
            n.pop(i)
        else:
            print('Элемент не найден')
    return n


    