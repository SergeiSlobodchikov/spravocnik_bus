import os
from sys import platform

bus = 'bus.txt'
route = 'route.txt'
driver = 'driver.txt'

commands = ['Вывод автобусов',
            'Добавление автобуса',
            'Вывод водителей',
            'Добавление водителей',
            'Вывод маршрута',
            'Добавление маршрута',
            'Поиск',
            'Удаление',
            'Выход',]

def clear_screen():
    #очистка экрана (кроссплатформенная)
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")  # для Linux & MacOS
    else:
        os.system("cls")    # для Windows

def main_menu():
    print('Главное меню')
    for i, item in enumerate(commands, 1):
        print(f'\t{i} {item}')
    choice = input('Выберите пункт меню: ')
    return choice

def create_new_driver():
    print('Новый водитель')
    name = input('Введите имя и фамилию: ')
    phone =input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def create_new_bus():
    print('Новый Автобус')
    name = input('Введите номер автобуса: ')
    size_bus =input('Введите размер автобуса: ')
    comment = input('Введите комментарий: ')
    return name, size_bus, comment

def create_new_route():
    print('Новый водитель')
    name = input('Введите номер маршрута: ')
    start =input('Начало маршрута: ')
    finish = input('Конец маршрута: ')
    return name, start, finish

def show_bus(data_list: list):
    if len(data_list) < 1:
        print('Пустой лист')
    else:
        print(f'\t№. {"Номер автобуса":20} {"Размер":10} {"Комментарий":15}')
        for i, contact in enumerate(data_list, 1):
                print(f'\t{i}. {contact[0]:20} {contact[1]:10} {contact[2]:15}')

def show_driver(data_list: list):
    if len(data_list) < 1:
        print('Пустой лист')
    else:
        print(f'\t№. {"Имя водителя":25} {"Телефон":15} {"Комментарий":20}')
        for i, contact in enumerate(data_list, 1):
                print(f'\t{i}. {contact[0]:25} {contact[1]:15} {contact[2]:20}')

def show_route(data_list: list):
    if len(data_list) < 1:
        print('Пустой лист')
    else:
        print(f'\t№. {"№ Маршрута":10} {"Начало маршрута":15} {"Конец маршрута":15} {"Водитель":20} {"номер автобуса":10}')
        for i, contact in enumerate(data_list, 1):
                print(f'\t{i}. {contact[0]:10} {contact[1]:15} {contact[2]:15} {contact[3]:20} {contact[4]:10}')

def show_route_index(data_list: list, index_list: list):
    if len(data_list) < 1:
        print('Пустой лист')
    else:
        print(f'\t№. {"№ Маршрута":10} {"Начало маршрута":15} {"Конец маршрута":15} {"Водитель":20} {"номер автобуса":10}{"Индекс":6}')
        for i, contact in enumerate(data_list, 1):
                print(f'\t{i}. {contact[0]:10} {contact[1]:15} {contact[2]:15} {contact[3]:20} {contact[4]:10}{index_list[i-1]:6}')


def show_driver_index(data_list: list, index_list: list):
    if len(data_list) < 1:
        print('Пустой лист')
    else:
        print(f'\t№. {"Имя водителя":25} {"Телефон":15} {"Комментарий":20}{"Индекс":6}')
        for i, contact in enumerate(data_list, 1):
                print(f'\t{i}. {contact[0]:25} {contact[1]:15} {contact[2]:20}{index_list[i-1]:6}')

def show_bus_index(data_list: list, index_list: list):
    if len(data_list) < 1:
        print('Пустой лист')
    else:
        print(f'\t№. {"Номер автобуса":10} {"Размер":10} {"Комментарий":20}{"Индекс":6}')
        for i, contact in enumerate(data_list, 1):
                print(f'\t{i}. {contact[0]:10} {contact[1]:10} {contact[2]:20}{index_list[i-1]:6}')

def choice_datafile():
    choice = input(f'Нажмите цифру поиска Водитель(1), Автобус(2), Маршрут(3)\n: ')
    return choice

def exit_in_menu():
    input(f'Enter выход в меню>: ')

def find_contact():
    find = input('Введите искомый элемент: ')
    return find

def show(choice, my_list: list):
  if choice == "1":
      show_driver(my_list)
  elif choice == "2":
      show_bus(my_list)
  elif choice == "3":
    show_route(my_list)

def show_index(choice, my_list: list, index_list: list):
    if choice == "1":
        show_driver_index(my_list, index_list)
    elif choice == "2":
        show_bus_index(my_list, index_list)
    elif choice == "3":
      show_route_index(my_list, index_list)