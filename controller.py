import view
import time
import model

bus = 'bus.txt'
route = 'route.txt'
driver = 'driver.txt'


def start():
    while (True):
        view.clear_screen()
        choice = view.main_menu()
        match choice:
            case "1":
                # вывод данных
                view.show_bus(model.read_data(bus))
                view.exit_in_menu()
            case "2":
                # добавление данных
                new_bus = list(view.create_new_bus())
                model.add_new_string(bus, new_bus)
                view.exit_in_menu()
            case "3":
                # вывод данных
                view.show_driver(model.read_data(driver))
                view.exit_in_menu()

            case "4":
                # добавление данных
                new_driver = list(view.create_new_driver())
                model.add_new_string(driver, new_driver)
                view.exit_in_menu()

            case "5":
                # вывод данных
                view.show_route(model.read_data(route))
                view.exit_in_menu()
            case "6":
                # добавление данных
                new_route = list(view.create_new_route())
                result, index = model.search_data(driver, str(input('Поиск водителя на маршрут: ')))
                view.show_driver_index(result, index)
                name_driver = model.select_info(driver, input('Введите индекс водителя: '))
                new_route.append(str(name_driver))
                result, index = model.search_data(
                    bus, str(input('Поиск Автобуса: ')))
                view.show_bus_index(result, index)
                num_bus = model.select_info(
                    bus, input('Введите индекс Автобуса: '))
                new_route.append(str(num_bus))
                if len(new_route) == 5:
                    model.add_new_string(route, new_route)
                view.exit_in_menu()
              
            case "7":
              #Поиск
              choice = view.choice_datafile()
              result, index_list = model.choice_action(choice)
              view.show(choice, result)
              view.exit_in_menu()
            case "8":
              #Удаление
              choice = view.choice_datafile()
              result, index_list = model.choice_action(choice)
              view.show_index(choice, result, index_list)
              model.delete_data(input('Введите индекс: '), choice)
              view.exit_in_menu()
            case "9":
                # выход
                exit(0)
            case _:
                print("неверный ввод")
                time.sleep(3)

