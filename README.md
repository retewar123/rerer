[pobeg_ot_pudzha_v2 (1).py](https://github.com/user-attachments/files/34285228/pobeg_ot_pudzha_v2.1.py)
# Практическая работа №6
# Текстовая игра «Побег от Пуджа»

import random

# Словарь
ITEMS = {
    "фонарик": "Помогает видеть в тёмных местах.",
    "ключ": "Открывает ворота лагеря.",
    "карта": "Показывает безопасную дорогу через лес.",
    "верёвка": "Помогает преодолеть препятствие.",
    "аптечка": "Восстанавливает 30 единиц здоровья.",
    "аккумулятор": "Нужен для запуска автомобиля.",
    "канистра бензина": "В ней есть топливо для автомобиля.",
    "ключ от машины": "Подходит к замку автомобиля."
}

# Кортеж
LOCATIONS = (
    "Заброшенный лагерь",
    "Тёмный лес",
    "Старый склад",
    "Заброшенная деревня",
    "Последний выход"
)

# Кортеж 
FOREST_ROUTE = ("прямо", "налево", "направо")


def create_player():
    """Создаёт игрока и его основные характеристики."""
    player = {
        "health": 100,
        "stamina": 50,
        "inventory": [],
        "found": set(),
        "completed": set()
    }
    return player

def line():
    """Печатает разделительную линию."""
    print("-" * 50)


def pause():
    """Делает паузу между игровыми событиями."""
    input("\nНажмите Enter, чтобы продолжить...")


def show_title():
    """Показывает название и краткое описание игры."""
    print("=" * 50)
    print("              ПОБЕГ ОТ ПУДЖА")
    print("=" * 50)
    print("Вы оказались на заброшенной территории.")
    print("Вам нужно пройти пять локаций и сбежать.")
    print("Пудж будет пытаться помешать вашему побегу.")
    print("Удачи! Она вам понадобится.")
    print("=" * 50)


def show_rules():
    """Объясняет правила игры."""
    line()
    print("ПРАВИЛА")
    print("1. Для выбора действия вводите его номер.")
    print("2. Следите за здоровьем и выносливостью.")
    print("3. Собирайте предметы: они пригодятся позже.")
    print("4. При встрече с Пуджем можно убежать или спрятаться.")
    print("5. Аптечка восстанавливает здоровье.")
    line()
    pause()


def get_choice(question, minimum, maximum):
    """Получает число от игрока и проверяет его."""
    while True:
        try:
            answer = int(input(question))
            if minimum <= answer <= maximum:
                return answer
            print("Выберите число от", minimum, "до", maximum)
        except ValueError:
            print("Нужно ввести число. Попробуйте ещё раз.")


def show_status(player):
    """Показывает здоровье, выносливость и пройденные уровни."""
    line()
    print("ЗДОРОВЬЕ:", player["health"], "/ 100")
    print("ВЫНОСЛИВОСТЬ:", player["stamina"], "/ 50")
    print("ПРОЙДЕНО УРОВНЕЙ:", len(player["completed"]), "/ 5")
    line()


def show_inventory(player):
    """Выводит предметы, которые собрал игрок."""
    line()
    print("ИНВЕНТАРЬ")
    if not player["inventory"]:
        print("Пока ничего нет.")
    else:
        for number, item in enumerate(player["inventory"], start=1):
            print(str(number) + ". " + item)
            print("   " + ITEMS[item])
    line()


def has_item(player, item):
    """Проверяет наличие предмета в инвентаре."""
    return item in player["inventory"]


def add_item(player, item):
    """Добавляет новый предмет в инвентарь."""
    if item in player["inventory"]:
        print("Этот предмет у вас уже есть.")
        return
    player["inventory"].append(item)
    player["found"].add(item)
    print("Вы нашли предмет:", item)
    print(ITEMS[item])


def damage_player(player, amount):
    """Уменьшает здоровье игрока."""
    player["health"] -= amount
    if player["health"] < 0:
        player["health"] = 0
    print("Вы потеряли", amount, "здоровья.")
    print("Осталось здоровья:", player["health"])


def use_medkit(player):
    """Использует аптечку, если она есть."""
    if not has_item(player, "аптечка"):
        print("У вас нет аптечки.")
        return
    if player["health"] == 100:
        print("Здоровье и так полное.")
        return
    player["inventory"].remove("аптечка")
    player["health"] += 30
    if player["health"] > 100:
        player["health"] = 100
    print("Вы использовали аптечку.")
    print("Текущее здоровье:", player["health"])


def rest_player(player):
    """Восстанавливает часть выносливости."""
    player["stamina"] += 15
    if player["stamina"] > 50:
        player["stamina"] = 50
    print("Вы немного отдохнули.")
    print("Выносливость:", player["stamina"])


def use_item_menu(player):
    """Позволяет открыть инвентарь и использовать аптечку."""
    show_inventory(player)
    print("1. Использовать аптечку")
    print("2. Вернуться")
    choice = get_choice("Ваш выбор: ", 1, 2)
    if choice == 1:
        use_medkit(player)


def check_health(player):
    """Проверяет, не закончилось ли здоровье."""
    if player["health"] <= 0:
        line()
        print("ПУДЖ ВАС НАСТИГ!")
        print("Побег не удался. Попробуйте ещё раз.")
        line()
        return False
    return True


def pudge_encounter(player):
    """Иногда встречает игрока с Пуджем."""
    # Пудж появляется при выпадении числа 1.
    if random.randint(1, 3) != 1:
        print("Кажется, поблизости никого нет.")
        return True

    line()
    print("ВЫ УСЛЫШАЛИ ШАГИ... ЭТО ПУДЖ!")
    print("1. Убежать")
    print("2. Спрятаться")
    choice = get_choice("Что будете делать? ", 1, 2)

    if choice == 1:
        if player["stamina"] >= 10:
            player["stamina"] -= 10
            print("Вы быстро убежали от Пуджа.")
        else:
            print("Вы устали и не смогли убежать!")
            damage_player(player, 20)
    else:
        if random.randint(1, 2) == 1:
            print("Пудж прошёл мимо и не заметил вас.")
        else:
            print("Пудж заметил ваше укрытие!")
            damage_player(player, 15)

    return check_health(player)


def level_start(number):
    """Показывает название и номер уровня."""
    line()
    print("УРОВЕНЬ", number, "—", LOCATIONS[number - 1].upper())
    line()


def level_one(player):
    """Первый уровень: поиск вещей в заброшенном лагере."""
    level_start(1)
    print("Вы просыпаетесь в старом лагере.")
    print("Где-то неподалёку слышен голос Пуджа.")
    print("Вам нужно найти фонарик и ключ от ворот.")

    while not (has_item(player, "фонарик") and has_item(player, "ключ")):
        print("\n1. Осмотреть палатку")
        print("2. Осмотреть старый ящик")
        print("3. Проверить состояние")
        choice = get_choice("Ваше действие: ", 1, 3)

        if choice == 1:
            if not has_item(player, "фонарик"):
                add_item(player, "фонарик")
            else:
                print("В палатке больше ничего нет.")
        elif choice == 2:
            if not has_item(player, "ключ"):
                add_item(player, "ключ")
            else:
                print("Ящик пуст.")
        else:
            show_status(player)
            show_inventory(player)

        if choice != 3 and not pudge_encounter(player):
            return False

    print("\nВы нашли всё необходимое.")
    print("С помощью ключа вы открываете ворота лагеря.")
    player["completed"].add(1)
    pause()
    return True


def level_two(player):
    """Второй уровень: поиск дороги через тёмный лес."""
    level_start(2)
    print("Вы вошли в тёмный лес.")
    print("Без карты здесь легко заблудиться.")
    print("Нужно найти карту и верёвку.")

    while not (has_item(player, "карта") and has_item(player, "верёвка")):
        print("\n1. Осмотреть поваленное дерево")
        print("2. Проверить старый рюкзак")
        print("3. Отдохнуть")
        choice = get_choice("Ваше действие: ", 1, 3)

        if choice == 1:
            if not has_item(player, "верёвка"):
                add_item(player, "верёвка")
            else:
                print("Под деревом больше ничего нет.")
        elif choice == 2:
            if not has_item(player, "карта"):
                add_item(player, "карта")
            else:
                print("Рюкзак пуст.")
        else:
            rest_player(player)

        if choice != 3 and not pudge_encounter(player):
            return False

    print("\nНа карте отмечен безопасный маршрут.")
    print("Введите три направления по очереди.")
    for direction in FOREST_ROUTE:
        answer = input("Куда идти? ").strip().lower()
        if answer != direction:
            print("Вы свернули не туда и потеряли время.")
            damage_player(player, 10)
            if not check_health(player):
                return False
        else:
            print("Верное направление!")

    print("Вы выбрались из леса.")
    player["completed"].add(2)
    pause()
    return True


def level_three(player):
    """Третий уровень: поиск деталей на старом складе."""
    level_start(3)
    print("Перед вами старый склад с закрытой дверью.")
    print("Внутри можно найти аккумулятор для машины.")

    while not has_item(player, "аккумулятор"):
        print("\n1. Осмотреть полки")
        print("2. Осмотреть стол")
        print("3. Проверить инвентарь")
        choice = get_choice("Ваше действие: ", 1, 3)

        if choice == 1:
            add_item(player, "аккумулятор")
        elif choice == 2:
            if not has_item(player, "аптечка"):
                add_item(player, "аптечка")
            else:
                print("На столе больше ничего нет.")
        else:
            show_inventory(player)

        if choice != 3 and not pudge_encounter(player):
            return False

    print("\nВы забрали аккумулятор.")
    print("Теперь можно двигаться дальше.")
    player["completed"].add(3)
    pause()
    return True


def level_four(player):
    """Четвёртый уровень: поиск бензина и ключа от машины."""
    level_start(4)
    print("Вы добрались до заброшенной деревни.")
    print("Здесь стоит старый гараж.")
    print("Для побега нужны бензин и ключ от машины.")

    while not (has_item(player, "канистра бензина") and
               has_item(player, "ключ от машины")):
        print("\n1. Осмотреть гараж")
        print("2. Осмотреть дом")
        print("3. Отдохнуть")
        choice = get_choice("Ваше действие: ", 1, 3)

        if choice == 1:
            if not has_item(player, "канистра бензина"):
                add_item(player, "канистра бензина")
            else:
                print("В гараже больше нет топлива.")
        elif choice == 2:
            if not has_item(player, "ключ от машины"):
                add_item(player, "ключ от машины")
            else:
                print("В доме больше ничего полезного нет.")
        else:
            rest_player(player)

        if choice != 3 and not pudge_encounter(player):
            return False

    print("\nВы нашли бензин и ключ от машины.")
    print("Осталось добраться до последнего выхода.")
    player["completed"].add(4)
    pause()
    return True


def level_five(player):
    """Пятый уровень: запуск машины и окончательный побег."""
    level_start(5)
    print("Перед вами стоит старая машина.")
    print("Пудж уже близко. Нужно срочно уезжать!")

    needed_items = ["аккумулятор", "канистра бензина", "ключ от машины"]
    print("Для запуска машины необходимы:")
    for item in needed_items:
        print("-", item)

    while True:
        print("\n1. Проверить детали")
        print("2. Попробовать завести машину")
        print("3. Использовать аптечку")
        choice = get_choice("Ваше действие: ", 1, 3)

        if choice == 1:
            for item in needed_items:
                if has_item(player, item):
                    print(item + " — есть")
                else:
                    print(item + " — отсутствует")
        elif choice == 2:
            all_parts_found = True
            for item in needed_items:
                if not has_item(player, item):
                    all_parts_found = False
            if all_parts_found:
                print("Вы вставили ключ и завели двигатель!")
                print("Машина тронулась с места.")
                print("Пудж остался далеко позади.")
                player["completed"].add(5)
                return True
            print("Не хватает необходимых деталей.")
            if not pudge_encounter(player):
                return False
        else:
            use_medkit(player)


def main_menu():
    """Показывает главное меню игры."""
    print("\nГЛАВНОЕ МЕНЮ")
    print("1. Новая игра")
    print("2. Правила")
    print("3. Выход")
    return get_choice("Выберите действие: ", 1, 3)


def play_game():
    """Запускает уровни по порядку."""
    player = create_player()
    levels = [level_one, level_two, level_three, level_four, level_five]

    for level in levels:
        if player["health"] <= 0:
            break
        result = level(player)
        if not result:
            break

    if len(player["completed"]) == 5 and player["health"] > 0:
        line()
        print("ПОЗДРАВЛЯЕМ! ВЫ СБЕЖАЛИ ОТ ПУДЖА!")
        print("Вы прошли все пять уровней.")
        print("Игра окончена. Победа!")
        line()
    else:
        check_health(player)


def main():
    """Главная функция, запускающая игру."""
    show_title()

    while True:
        choice = main_menu()

        if choice == 1:
            show_rules()
            play_game()
            pause()
        elif choice == 2:
            show_rules()
        else:
            print("Спасибо за игру! До встречи.")
            break


# Запуск программы начинается здесь.
if __name__ == "__main__":
    main()
