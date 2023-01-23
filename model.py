bus = 'bus.txt'
route = 'route.txt'
driver = 'driver.txt'

def add_new_string(name, new_contact: list):
    data_to_save = ",".join(new_contact)+"\n"
    print(data_to_save)
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_to_save)


def read_data(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result


def search_data(name, find: str):
    result = []
    index = 0
    index_list = []
    data = read_data(name)
    for string in data:
        for field in string:
            if find in field:
                result.append(string)
                index_list.append(index)
                break
        index += 1
    return result, index_list


def save_data_to_file(name, data_to_save):
    data_to_save = ",".join(data_to_save)+"\n"
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_to_save)


def change_data(name, change_data: str, choice: str):
    data_file = read_data(name)
    if change_data == '':
        return
    else:
        data_file[int(change_data)][int(choice)] = input('Введите: ')
        with open(name, 'w', encoding='utf8') as data:
            data.write('')
        for i in data_file:
            save_data_to_file(name, i)


def select_info(name, index: str):
    data_file = read_data(name)
    if change_data == '':
        return
    else:
        word = data_file[int(index)][int(0)]
        return word


def choice_action(choice):
  if choice == '1':
    result, index_list = search_data(driver, str(input('Поиск водителя: ')))
    return result, index_list
  elif choice == '2':
    result, index_list = search_data(bus, str(input('Автобус: ')))
    return result, index_list
  elif choice == '3':
    result, index_list = search_data(route, str(input('Маршрут: ')))
    return result, index_list
  else:  
    print('Неправильно')



def delete_data(delete_contact: str, choice):
    if choice == '1':
      data_file = read_data(driver)
      path = driver
    elif choice == '2':
      data_file = read_data(bus)
      path = bus
    elif choice == '3':
      data_file = read_data(route)
      path = route
    if delete_contact == '':
        return
    else:
        data_file.pop(int(delete_contact))
        with open(path, 'w', encoding='utf8') as data:
            data.write('')
        for i in data_file:
            save_data_to_file(path, i)