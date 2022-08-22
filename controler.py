from interface import Interface
import inputt 
import seach
import delll
import change
import outputt
import exp
import inporttt
import safe

def Controler():
    regim = int(input(Interface()))
    if regim == 1:
        print('Вы открыли меню для ввода нового сотрудника')
        res = inputt.User_Data()
        return Interface()
    elif regim == 2:
        print('Вы открыли меню поиска сотрудников')
        res = seach.Seach_Name()
        return Interface()
    elif regim == 3:
        print('Вы открыли меню удаления сотрудника из базы')
        res = delll.Del()
        return Interface()
    elif regim == 4:
        print('Меню для поиска и изменения данных сотрудника запущено')
        res = change.Seach_Name()
        return Interface()
    elif regim == 5:
        print('Режим вывода базы данных на экран запущен')
        res = outputt.Print_Data() 
        return Interface()
    elif regim == 6:
        print('Вы запустили режим экспорта базы')
        res = exp.export_data() 
        return Interface()
    elif regim == 7:
        print('Вы запустили режим импорта базы')
        print('Выберите файл для импорта: 11. Сотрудники; 12. Отдел; 13. Должность')
        im = int(input())
        if im == 11: res = inporttt.Load_FIO()
        elif im == 12: res = inporttt.Load_Otdel()
        elif im == 13: res = inporttt.Load_Post()
        else: print('Введите корректные данные')
        return Interface()
    elif regim == 8:
        print('Вы запустили режим сохранения данных')
        print('Выберите файл для сохранения: 21. Сотрудники; 22. Отдел; 23. Должность')
        im = int(input())
        if im == 21: res = safe.Safe_FIO()
        elif im == 22: res = safe.Safe_otdel
        elif im == 23: res = safe.Safe_post()
        else: print('Введите корректные данные')
        return Interface()
    elif regim == 9:
        print('Режим выхода из программы запущен')
        res = exit()
    else:
        print('Выберите корректный режим работы')
    return res

