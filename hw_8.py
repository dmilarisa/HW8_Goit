from datetime import datetime, timedelta

def congratulate(users):
    now_day = datetime.now()

    # Визначаємо дату наступного понеділка
    next_monday = now_day + timedelta(7 - now_day.weekday())

    # Визначаємо цільові дати найближчого тижня для привітань - ті, що потраплять до понеділка, та окремо ті, що потраплять до інших днів тижня
    target_dates_monday = [next_monday - timedelta(2),
                    next_monday - timedelta(1),
                    next_monday]
    target_dates_other_days = [next_monday + timedelta(1),
                    next_monday + timedelta(2),
                    next_monday + timedelta(3),
                    next_monday + timedelta(4)]
    
    # Складаэмо список, в якому будемо записувати результати - це за умовою, хоча я в обрала краще словник, а не список
    birth_list = [['Monday: ',[]], ['Tusday: ',[]], ['Wednesday: ',[]],['Thirsday: ',[]],['Friday: ',[]]]

    # Перебираємо наш словник з людьми та порівнюємо з днями народження цільового списку
    for user in users:
        for d in target_dates_monday:
            if user['birthday'].day == d.day and user['birthday'].month == d.month:
                birth_list[0][1].append(user['name'])
        for d in target_dates_other_days:
            if user['birthday'].day == d.day and user['birthday'].month == d.month:
                day_of_week = d.weekday()
                birth_list[day_of_week][1].append(user['name'])    
    
    #Друкуємо в консоль отриманий список у заданому умовою форматі
    for el in birth_list:
        if len(el[1]) != 0:
            str_for_print = el[0]
            for name in el[1]:
                str_for_print += name + ', '
            print(str_for_print[:-2])

# Це тестовий словник з людьми та днями народження        
users = [{'name': 'John Ray', 'birthday': datetime(day = 25, month = 5, year = 1997)},
         {'name': 'Helen Born', 'birthday': datetime(day = 27, month = 5, year = 1978)},
         {'name': 'Hu Yang', 'birthday': datetime(day = 22, month = 5, year = 1978)}, 
         {'name': 'Megan Fox', 'birthday': datetime(day = 16, month = 5, year = 1986)},
         {'name': 'Steven Smith', 'birthday': datetime(day = 19, month = 5, year = 1989)},
         {'name': 'Helena Bonham Carter', 'birthday': datetime(day = 26, month = 5, year = 1990)},
         {'name': 'Pam Grier', 'birthday': datetime(day = 26, month = 5, year = 1990)},
         {'name': 'Jack Colar', 'birthday': datetime(day = 26, month = 1, year = 2005)},
         {'name': 'Joan Cordoso', 'birthday': datetime(day = 23, month = 5, year = 2004)},
        ]

congratulate(users)   


