# =====================================================================
# НАЧАЛЬНЫЕ ДАННЫЕ И КОЛЛЕКЦИИ (КОРТЕЖИ, СПИСКИ, МНОЖЕСТВА, СЛОВАРИ)
# =====================================================================

# КОРТЕЖИ: неизменяемые базовые параметры игры
PLAYER_BASE_STATS = (100, 50, 10)  # (Здоровье, Мана, Скорость)
HOOK_DIRECTIONS = ("север", "восток", "юг", "запад")
SAFE_COORDINATES = ((1, 2), (2, 3), (3, 1))

# СПИСКИ: инвентарь игрока, добыча и история действий
inventory = ["Танго", "Свиток телепортации"]
river_items = ["Вард", "Блинк Даггер", "Фласка"]
forest_obstacles = ["Стая волков", "Заросли терновника", "Крип-маг"]
game_history = []

# МНОЖЕСТВА: посещенные зоны, решенные загадки и открытые вентили
visited_locations = set()
activated_runes = set()
opened_valves = set()
disarmed_traps = set()

# СЛОВАРИ: базы знаний предметов, характеристики монстра и загадки
item_details = {
    "Танго": {"type": "heal", "value": 35, "desc": "Восстанавливает 35 HP."},
    "Свиток телепортации": {"type": "escape", "value": 1, "desc": "Телепортирует на базу."},
    "Вард": {"type": "vision", "value": 100, "desc": "Дает обзор и предупреждает о хуке."},
    "Блинк Даггер": {"type": "mobility", "value": 50, "desc": "Мгновенный скачок вперед."},
    "Фласка": {"type": "heal", "value": 60, "desc": "Целебная мазь, восстанавливает 60 HP."},
    "Сыр": {"type": "full_heal", "value": 100, "desc": "Легендарный сыр, восстанавливает 100 HP."}
}

pudge_state = {
    "name": "Мясник Пудж",
    "distance": 8,
    "rot_damage": 12
}

riddles = {
    "руна_мудрости": {
        "вопрос": "Что всегда идет вперед, но никогда не делает шага назад?",
        "ответ": "время"
    },
    "древний_пень": {
        "вопрос": "Без ног бежит, без крыльев летит, туман разгоняет. Что это?",
        "ответ": "ветер"
    },
    "алтарь_крови": {
        "вопрос": "Чем больше из меня берешь, тем больше я становлюсь. Что я?",
        "ответ": "яма"
    }
}

# Текущее состояние героя
current_hp = PLAYER_BASE_STATS[0]
current_mana = PLAYER_BASE_STATS[1]

# Счетчики для игрового цикла и вычислений траекторий
step_counter = 0
game_running = True
current_level = 1

# =====================================================================
# ВСТУПЛЕНИЕ
# =====================================================================
print("=" * 65)
print("       ПОБЕГ ИЗ ТЕМНОГО ЛЕСА: ОХОТА ПУДЖА")
print("=" * 65)
print("Вы очнулись посреди мутной ледяной реки.")
print("Вокруг непроглядный туман войны.")
print("Внезапно из темноты раздается зловещее:")
print("'СВЕЖЕЕ МЯСООО!..'")
print("Слышен звон ржавой цепи. Пудж начал охоту!")
print("Цель: преодолеть 4 уровня и добежать до союзного Фонтана.\n")

# =====================================================================
# ГЛАВНЫЙ ИГРОВОЙ ЦИКЛ (БЕЗ DEF)
# =====================================================================
while game_running:
    step_counter += 1

    # -----------------------------------------------------------------
    # ЭТАП 1: МУТНАЯ РЕКА И ПЕРВЫЙ ХУК
    # -----------------------------------------------------------------
    if current_level == 1:
        visited_locations.add("Мутная река")
        print("\n--- [ЭТАП 1: МУТНАЯ РЕКА] ---")
        print(f"Ваше здоровье: {current_hp}/{PLAYER_BASE_STATS[0]} HP | Дистанция до Пуджа: {pudge_state['distance']} м.")
        print("В воде возле камышей видны выброшенные вещи.")
        print("Действия:")
        print("1. Обыскать речную отмель")
        print("2. Проверить инвентарь")
        print("3. Использовать предмет")
        print("4. Прорываться сквозь туман к Лесу")

        choice = input("\nВыберите действие (1-4): ").strip()

        if choice == "1":
            if len(river_items) > 0:
                found_item = river_items.pop(0)
                inventory.append(found_item)
                game_history.append(f"Найден предмет: {found_item}")
                print(f"\n[+] Вы выловили из тины: {found_item}!")
                print("Справка:", item_details[found_item]["desc"])
            else:
                print("\nНа отмели больше ничего нет, только ил.")

        elif choice == "2":
            print(f"\nВаш инвентарь (элементов: {len(inventory)}):")
            for i in range(len(inventory)):
                itm_name = inventory[i]
                itm_desc = item_details[itm_name]["desc"]
                print(i + 1, "-", itm_name, ":", itm_desc)

        elif choice == "3":
            if len(inventory) == 0:
                print("\nИнвентарь пуст!")
            else:
                print("\nКакой предмет использовать?")
                for i in range(len(inventory)):
                    print(i + 1, "-", inventory[i])

                raw_choice = input("Введите номер предмета (или 0 для отмены): ").strip()
                try:
                    num = int(raw_choice)
                    if 1 <= num <= len(inventory):
                        used = inventory.pop(num - 1)
                        if used == "Танго":
                            current_hp += item_details["Танго"]["value"]
                            if current_hp > PLAYER_BASE_STATS[0]:
                                current_hp = PLAYER_BASE_STATS[0]
                            print(f"\nВы съели дерево. Здоровье: {current_hp} HP.")
                        elif used == "Фласка":
                            current_hp += item_details["Фласка"]["value"]
                            if current_hp > PLAYER_BASE_STATS[0]:
                                current_hp = PLAYER_BASE_STATS[0]
                            print(f"\nВы намазались мазью. Здоровье: {current_hp} HP.")
                        elif used == "Вард":
                            activated_runes.add("Обзор реки")
                            print("\nВы установили Вард! Теперь замах хука Пуджа виден в тумане.")
                        else:
                            print(f"\nВы не можете использовать {used} здесь. Предмет потрачен впустую.")
                    else:
                        print("Действие отменено.")
                except ValueError:
                    print("Ошибка: нужно ввести целое число!")

        elif choice == "4":
            print("\nВы бежите по пояс в воде к темнеющему лесному склону...")
            print("Сзади рассекает воздух тяжелый мясницкий крюк!")

            # Направление вычисляется по формуле с остатком от деления
            pudge_direction_idx = (step_counter * 3 + 1) % 4
            pudge_direction = HOOK_DIRECTIONS[pudge_direction_idx]

            if "Обзор реки" in activated_runes:
                print(f"[Вард раскрыл замах!] Пудж кидает крюк на: {pudge_direction.upper()}!")

            print("Куда сделать спасительный рывок?")
            for d in HOOK_DIRECTIONS:
                print("-", d)
            dodge = input("Ваше направление: ").strip().lower()

            if dodge == pudge_direction:
                print("\n[УДАР!] Крюк вонзается прямо вам в спину!")
                damage = 40
                current_hp -= damage
                pudge_state["distance"] -= 3
                print(f"Вы потеряли {damage} HP! Пудж подтягивает вас ближе!")
                if current_hp <= 0:
                    print("\nПудж разрубает вас тесаком... ВЫ ПОГИБЛИ!")
                    game_running = False
            else:
                print("\n[УСПЕХ!] Крюк со свистом пролетает мимо и крошит камни!")
                print("Вы выбираетесь на берег Леса Скверны.")
                current_level = 2

        else:
            print("Неверный ввод. Пудж приближается, пока вы медлите!")
            pudge_state["distance"] -= 1

    # -----------------------------------------------------------------
    # ЭТАП 2: ЛЕС СКВЕРНЫ И РУННЫЕ ОБЕЛИСКИ
    # -----------------------------------------------------------------
    elif current_level == 2:
        visited_locations.add("Лес Скверны")
        print("\n--- [ЭТАП 2: ЛЕС СКВЕРНЫ] ---")
        print(f"Ваше здоровье: {current_hp}/{PLAYER_BASE_STATS[0]} HP | Дистанция: {pudge_state['distance']} м.")
        print("Посещенные места:", visited_locations)
        print("Впереди тропу преграждают заросли и древний магический камень.")
        print("Преграды в чаще:", forest_obstacles)
        print("Действия:")
        print("1. Разгадать загадку Обелиска (открыть тайный проход)")
        print("2. Проверить инвентарь и применить предмет")
        print("3. Прорываться через лесные препятствия силой")
        print("4. Осмотреться вокруг")

        choice = input("\nВыберите действие (1-4): ").strip()

        if choice == "1":
            # Ищем нерешенную загадку через цикл по ключам словаря
            found_riddle_key = ""
            for r_key in riddles:
                if r_key not in activated_runes:
                    found_riddle_key = r_key
                    break

            if found_riddle_key == "":
                print("\nВсе обелиски уже активированы! Проход свободен.")
                current_level = 3
            else:
                q_text = riddles[found_riddle_key]["вопрос"]
                q_ans = riddles[found_riddle_key]["ответ"]
                print(f"\nНа камне высечены руны: '{q_text}'")
                user_answer = input("Ваш ответ (одним словом): ").strip().lower()

                if user_answer == q_ans:
                    print("[ВЕРНО!] Камень засиял лазурным пламенем. Стена ветвей опала!")
                    activated_runes.add(found_riddle_key)
                    if len(activated_runes) >= 2:
                        print("Вы открыли короткий путь в катакомбы и оторвались от Пуджа!")
                        pudge_state["distance"] += 4
                        current_level = 3
                else:
                    print("[ОШИБКА!] Камень ударил вас магической молнией!")
                    current_hp -= 20
                    pudge_state["distance"] -= 2
                    print(f"Вы потеряли 20 HP. Пудж подошел ближе! Осталось HP: {current_hp}")
                    if current_hp <= 0:
                        print("\nЭнергия рун испепелила вас. ВЫ ПОГИБЛИ!")
                        game_running = False

        elif choice == "2":
            print(f"\nИнвентарь: {inventory}")
            use_item = input("Введите точное название предмета: ").strip()
            if use_item in inventory:
                if use_item == "Танго":
                    inventory.remove("Танго")
                    current_hp += 35
                    if current_hp > PLAYER_BASE_STATS[0]:
                        current_hp = PLAYER_BASE_STATS[0]
                    print(f"Вы съели дерево. Здоровье: {current_hp} HP.")
                elif use_item == "Блинк Даггер":
                    inventory.remove("Блинк Даггер")
                    print("Вы телепортируетесь через гущу леса прямо ко входу в катакомбы!")
                    pudge_state["distance"] += 5
                    current_level = 3
                elif use_item == "Фласка":
                    inventory.remove("Фласка")
                    current_hp += 60
                    if current_hp > PLAYER_BASE_STATS[0]:
                        current_hp = PLAYER_BASE_STATS[0]
                    print(f"Вы восстановили здоровье. Теперь HP: {current_hp}")
                else:
                    print("Этот предмет сейчас не поможет.")
            else:
                print("Такого предмета нет в инвентаре.")

        elif choice == "3":
            if len(forest_obstacles) > 0:
                removed_obstacle = forest_obstacles.pop(0)
                print(f"\nВы с боем прорываетесь сквозь: {removed_obstacle}!")
                dmg = 18
                current_hp -= dmg
                print(f"Вы преодолели преграду, потеряв {dmg} HP. Текущее HP: {current_hp}")
                if current_hp <= 0:
                    print("\nЛес поглотил ваши силы... ВЫ ПОГИБЛИ!")
                    game_running = False
                elif len(forest_obstacles) == 0:
                    print("Вы прорубили путь к заброшенным катакомбам!")
                    current_level = 3
            else:
                print("Препятствий на пути больше нет! Вы бежите вперед.")
                current_level = 3

        elif choice == "4":
            print("\nВы всматриваетесь в чащу леса.")
            print("Деревья с треском падают. Пудж прорубает путь своим огромным тесаком!")
            pudge_state["distance"] -= 1

        else:
            print("Неверный выбор.")

    # -----------------------------------------------------------------
    # ЭТАП 3: ЗАТОПЛЕННЫЕ КАТАКОМБЫ И ЯДОВИТЫЙ ГАЗ (ROT)
    # -----------------------------------------------------------------
    elif current_level == 3:
        visited_locations.add("Катакомбы")
        print("\n--- [ЭТАП 3: КАТАКОМБЫ ПУДЖА] ---")
        print(f"Ваше здоровье: {current_hp} HP | Дистанция: {pudge_state['distance']} м.")
        print("В узких коридорах стоит едкий зеленый туман: Пудж включил гниль (Rot)!")
        print(f"Открытые вентили: {opened_valves} (Для сброса давления нужно открыть: '1', '2' и '3')")
        print("Действия:")
        print("1. Повернуть вентиль шлюза")
        print("2. Осмотреть безопасные плиты пола")
        print("3. Лечение предметами из инвентаря")
        print("4. Прорываться к гермодвери")

        # Получаем урон от газа каждый шаг на 3 этапе
        current_hp -= pudge_state["rot_damage"]
        print(f"[ЯД] Вы вдыхаете яд и теряете {pudge_state['rot_damage']} HP! Здоровье: {current_hp}")
        if current_hp <= 0:
            print("\nВы задохнулись в ядовитых испарениях Пуджа... ВЫ ПОГИБЛИ!")
            game_running = False
            continue

        choice = input("\nВыберите действие (1-4): ").strip()

        if choice == "1":
            valve_num = input("Какой вентиль повернуть (1, 2 или 3)? ").strip()
            if valve_num == "1" or valve_num == "2" or valve_num == "3":
                if valve_num in opened_valves:
                    print("Этот вентиль уже выкручен до упора!")
                else:
                    opened_valves.add(valve_num)
                    print(f"Вентиль {valve_num} со скрипом поддался! Часть яда выветрилась в шахту.")
                    if len(opened_valves) == 3:
                        print("Все вентили открыты! Воздух очищен, а массивная дверь со щелчком отперта!")
            else:
                print("Такого вентиля нет на стене.")

        elif choice == "2":
            print("\nВы осматриваете каменные плиты пола.")
            print("Введите координаты для поиска тайника:")
            try:
                coord_x = int(input("Координата X (от 1 до 3): ").strip())
                coord_y = int(input("Координата Y (от 1 до 3): ").strip())
                check_coord = (coord_x, coord_y)

                if check_coord in SAFE_COORDINATES:
                    if "Сыр" not in inventory:
                        print(f"В нише плиты {check_coord} вы нашли запечатанную головку Сыра!")
                        inventory.append("Сыр")
                    else:
                        print("Этот тайник уже пуст.")
                else:
                    print(f"Щелк! Плита {check_coord} оказалась ловушкой с шипами!")
                    current_hp -= 15
                    pudge_state["distance"] -= 2
                    print(f"Вы потеряли 15 HP. Осталось HP: {current_hp}")
                    if current_hp <= 0:
                        print("Ловушка добила вас... ВЫ ПОГИБЛИ!")
                        game_running = False
            except ValueError:
                print("Ошибка: координаты должны быть целыми числами!")

        elif choice == "3":
            if "Сыр" in inventory:
                inventory.remove("Сыр")
                current_hp = PLAYER_BASE_STATS[0]
                print(f"Вы съели Сыр! Здоровье полностью восстановлено: {current_hp} HP!")
            elif "Фласка" in inventory:
                inventory.remove("Фласка")
                current_hp += 60
                if current_hp > PLAYER_BASE_STATS[0]:
                    current_hp = PLAYER_BASE_STATS[0]
                print(f"Вы применили Фласку. HP: {current_hp}")
            elif "Танго" in inventory:
                inventory.remove("Танго")
                current_hp += 35
                if current_hp > PLAYER_BASE_STATS[0]:
                    current_hp = PLAYER_BASE_STATS[0]
                print(f"Вы применили Танго. HP: {current_hp}")
            else:
                print("Лечащих предметов в рюкзаке нет!")

        elif choice == "4":
            if len(opened_valves) >= 2:
                print("\nВы наваливаетесь на приоткрытую дверь и протискиваетесь в проем!")
                current_level = 4
            else:
                print("\nДверь намертво заклинило давлением! Нужно открыть минимум 2 вентиля!")
                pudge_state["distance"] -= 1

        else:
            print("В панике вы мечетесь по комнате.")

    # -----------------------------------------------------------------
    # ЭТАП 4: ФИНАЛЬНЫЙ МОСТ И СПАСЕНИЕ У ФОНТАНА
    # -----------------------------------------------------------------
    elif current_level == 4:
        visited_locations.add("Мост к Фонтану")
        print("\n--- [ЭТАП 4: МОСТ К ФОНТАНУ - ФИНАЛ] ---")
        print("Впереди возвышаются сияющие башни и родной Фонтан Сил Света!")
        print(f"Пудж дышит прямо в затылок! Расстояние: {pudge_state['distance']} метров.")
        print(f"Ваше текущее здоровье: {current_hp} HP.")

        print("\nПудж раскручивает ржавую цепь для решающего броска крюка!")
        print("Ваши действия:")
        print("1. Активировать Свиток телепортации")
        print("2. Совершить акробатический маневр уклонения")
        print("3. Бросить во врага вещи из инвентаря")

        final_choice = input("\nСделайте решающий выбор (1-3): ").strip()

        if final_choice == "1":
            if "Свиток телепортации" in inventory:
                print("\nВы сжимаете в руке свиток...")
                print("Вокруг вашего тела вспыхивают золотые кольца магии!")
                print("Пудж швыряет крюк, но он рассекает воздух ровно через долю секунды после телепортации!")
                print("\n" + "=" * 65)
                print("     ВСПЫШКА СВЕТА! ВЫ ОКАЗАЛИСЬ НА ФОНТАНЕ!")
                print("     ПУДЖ БЕССИЛЬНО РЫЧИТ В ТЕМНОТЕ! ПОБЕДА!")
                print("=" * 65)
                game_running = False
            else:
                print("\nУ вас нет свитка в инвентаре! Вы потратили драгоценные секунды!")
                pudge_state["distance"] = 0

        elif final_choice == "2":
            print("\nВы готовитесь прыгнуть за каменные колонны моста...")
            print("Безопасные точки из ваших записей:", SAFE_COORDINATES)
            try:
                dodge_x = int(input("Введите координату укрытия X: ").strip())
                dodge_y = int(input("Введите координату укрытия Y: ").strip())
                player_point = (dodge_x, dodge_y)

                # Проверяем, входит ли введенный кортеж в кортеж безопасных координат
                if player_point in SAFE_COORDINATES:
                    print("\n[ВЕЛИКОЛЕПНЫЙ ДОДЖ!]")
                    print("Крюк Пуджа с грохотом разносит гранитную колонну рядом с вами!")
                    print("Башни Фонтана фиксируют монстра и выпускают залп магических зарядов!")
                    print("Пудж в панике бежит обратно в чащу леса!")
                    print("\n" + "=" * 65)
                    print("          ВЫ ДОБРАЛИСЬ ЖИВЫМ! ПОЛНАЯ ПОБЕДА!")
                    print("=" * 65)
                    game_running = False
                else:
                    print("\nВы прыгнули прямо под траекторию броска!")
                    current_hp -= 85
                    print(f"Хук нанес вам 85 урона! Остаток здоровья: {current_hp} HP.")
                    if current_hp <= 0:
                        print("Пудж затаскивает вас во тьму... ВЫ ПОГИБЛИ!")
                        game_running = False
                    else:
                        print("Истекая кровью, вы вползаете под защитный купол Фонтана!")
                        print("Фонтан моментально исцеляет ваши раны и обращает врага в бегство!")
                        print("\nПОБЕДА НА ПОСЛЕДНЕМ ДЫХАНИИ!")
                        game_running = False
            except ValueError:
                print("Паника затуманила разум: вы споткнулись!")
                pudge_state["distance"] = 0

        elif final_choice == "3":
            if len(inventory) > 0:
                print(f"\nВы швыряете все предметы из сумки ({inventory}) прямо в лицо чудовищу!")
                print("Пудж ослеплен содержимым флаконов, оступается на краю моста и летит вниз в реку!")
                print("Вы спокойно шагаете к союзному Трону.")
                print("\n" + "=" * 65)
                print("           ВЫ ПЕРЕХИТРИЛИ МЯСНИКА! ПОБЕДА!")
                print("=" * 65)
                game_running = False
            else:
                print("\nВам нечего бросить! Рюкзак пуст!")
                pudge_state["distance"] = 0

        else:
            print("Нерешительность стоит вам жизни!")
            pudge_state["distance"] = 0

        # Если дистанция сократилась до нуля
        if pudge_state["distance"] <= 0 and game_running:
            print("\nПудж настигает вас широким шагом...")
            print("'DISMEMBER!' — тесак опускается вниз...")
            print("ВЫ ПОГИБЛИ!")
            game_running = False

# =====================================================================
# ИТОГОВАЯ СТАТИСТИКА (ВЫВОД КОЛЛЕКЦИЙ ИЗ КОНСПЕКТА)
# =====================================================================
print("\n" + "-" * 40)
print("       ИТОГИ ИГРОВОЙ СЕССИИ")
print("-" * 40)
print("Посещенные зоны (множество/set):", visited_locations)
print("Активированные руны (множество/set):", activated_runes)
print("Остаток предметов (список/list):", inventory)
print("Записи приключения (список/list):", game_history)
print("Количество сделанных ходов:", step_counter)
print("Игра завершена. Спасибо за прохождение!")