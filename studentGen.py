# ---------------------------------------------------------------------------------------------------------------------
# ЭТОТ ФАЙЛ СОЗДАЕТ СПИСОК СТУДЕНТОВ: СПИСОК 4 ГРУПП, ОЦЕНКИ ЗА ЗАЧЁТ И ЭКЗАМЕН. ТАКЖЕ ЗДЕСЬ ХРАНИТСЯ СПИСОК ДИСЦИПИН
# ---------------------------------------------------------------------------------------------------------------------
import random

student_male_name = ["Иван", "Олег", "Василий", "Евгений", "Константин", "Виктор", "Александр", "Антон", "Игорь",
                     "Дмитрий", "Владислав", "Даниил", "Михаил", "Арсений"]
student_female_name = ["Алина", "Арина", "Анастасия", "Валентина", "Валерия", "Дарья", "Елена", "Екатерина",
                       "Елизавета", "Ирина", "Любовь", "Маргарита", "Наталья", "Светлана"]
student_surname = ["Иванов", "Петров", "Васильев", "Морозов", "Тягунов", "Романов", "Корнев", "Кузнецов", "Михайлов",
                   "Смирнов", "Попов", "Карпов", "Гуляев", "Маслов"]
student_father_name = ["Иванович", "Олегович", "Васильевич", "Евгеньевич", "Константинович", "Викторович",
                       "Александрович", "Антонович", "Игоревич", "Дмитриевич", "Владиславович", "Даниилович",
                       "Михайлович", "Арсеньевич"]
student_list = []  # случайно сгенерированный список студентов

group1_1 = []  # 1 курс 1 группа
group1_2 = []  # 1 курс 2 группа
group2_1 = []  # 2 курс 1 группа
group2_2 = []  # 2 курс 2 группа
exams = []  # список экзаменов
zachet = []  # список зачётов
diciplines = [
    {'cipher': 2000,
     'name': 'Информационные системы в мехатронике и робототехнике',
     'hours': 200},
    {'cipher': 2001,
     'name': 'Агентно-ориентированные системы управления',
     'hours': 200},
    {'cipher': 2002,
     'name': 'Методы и теория оптимизации',
     'hours': 200},
    {'cipher': 2003,
     'name': 'Стандартизация в управлении качеством на предприятии',
     'hours': 200},

    {'cipher': 3000,
     'name': 'Теория игр в управлении роботами',
     'hours': 150},
    {'cipher': 3001,
     'name': 'Статистическая динамика автоматических систем',
     'hours': 150},
    {'cipher': 3002,
     'name': 'Коммуникативные технологии в профессиональной сфере на иностранном языке',
     'hours': 150},
    {'cipher': 3003,
     'name': 'Системный подход в научно-проектной деятельности',
     'hours': 150},

    {'cipher': 2100,
     'name': 'Автоматизация настройки систем управления интеллектуальных мобильных роботов',
     'hours': 200},
    {'cipher': 2101,
     'name': 'Системы автоматизированного проектирования и производства',
     'hours': 200},
    {'cipher': 2102,
     'name': 'Интеллектуальные технологии локальной навигации',
     'hours': 200},

    {'cipher': 3100,
     'name': 'Технологии обработки информации в интеллектуальных мобильных роботах',
     'hours': 150},
    {'cipher': 3101,
     'name': 'Теория эксперимента в исследованиях систем',
     'hours': 150},
    {'cipher': 3102,
     'name': 'Бизнес технологии цифрового производства',
     'hours': 150},
    {'cipher': 3103,
     'name': 'Управление проектами по созданию сложных технических систем',
     'hours': 150}
]  # список дисциплин

cipher_counter = 1000  # шифр студента


def generate(group_arr, course, group):
    global cipher_counter
    for i in range(20):  # в группе 20 студентов

#############################################   ФОРМИРОВАНИЕ СПИСКА ГРУППЫ   ###########################################

        gender = random.randint(0, 1)  # выбор пола студента, 0 - мужской, 1 - женский
        if gender == 0:
            a = {'student cipher': cipher_counter,
                 'name': random.choice(student_male_name),
                 'surname': random.choice(student_surname),
                 'father name': random.choice(student_father_name),
                 'course': course,
                 'group': group
                 }
        else:
            a = {'student cipher': cipher_counter,
                 'name': random.choice(student_female_name),
                 'surname': random.choice(student_surname) + 'а',
                 'father name': random.choice(student_father_name)[:-2] + 'на',
                 'course': course,
                 'group': group
                 }
        group_arr.append(a)

        ################################################   ОЦЕНКИ ЗА ЭКЗАМЕН   #################################################
        # для 1 курса шифр начинается с 2000, для 2 курса с 2100
        if course == 1:
            b = {'student cipher': cipher_counter,
                 'date': '10.01.23',
                 'subject cipher': 2000,
                 'mark': random.randint(2, 5)
                 }
            exams.append(b)
            b = {'student cipher': cipher_counter,
                 'date': '12.01.23',
                 'subject cipher': 2001,
                 'mark': random.randint(2, 5)
                 }
            exams.append(b)
            b = {'student cipher': cipher_counter,
                 'date': '14.01.23',
                 'subject cipher': 2002,
                 'mark': random.randint(2, 5)
                 }
            exams.append(b)
        elif course == 2:
            b = {'student cipher': cipher_counter,
                 'date': '10.01.23',
                 'subject cipher': 2100,
                 'mark': random.randint(2, 5)
                 }
            exams.append(b)
            b = {'student cipher': cipher_counter,
                 'date': '12.01.23',
                 'subject cipher': 2101,
                 'mark': random.randint(2, 5)
                 }
            exams.append(b)
            b = {'student cipher': cipher_counter,
                 'date': '14.01.23',
                 'subject cipher': 2102,
                 'mark': random.randint(2, 5)
                 }
            exams.append(b)

        #################################################   ОЦЕНКИ ЗА ЗАЧЁТ   ##################################################
        # для 1 курса шифр начинается с 3000, для 2 курса с 3100
        if course == 1:  # 0 - зачет не сдан, 1 - сдан
            b = {'student cipher': cipher_counter,
                 'date': '20.12.22',
                 'subject cipher': 3000,
                 'mark': random.choice([0, 1, 1, 1, 1])
                 }
            zachet.append(b)
            b = {'student cipher': cipher_counter,
                 'date': '22.12.22',
                 'subject cipher': 3001,
                 'mark': random.choice([0, 1, 1, 1, 1])
                 }
            zachet.append(b)
            b = {'student cipher': cipher_counter,
                 'date': '24.12.22',
                 'subject cipher': 3002,
                 'mark': random.choice([0, 1, 1, 1, 1])
                 }
            zachet.append(b)
            b = {'student cipher': cipher_counter,
                 'date': '26.12.22',
                 'subject cipher': 3003,
                 'mark': random.choice([0, 1, 1, 1, 1])
                 }
            zachet.append(b)
        elif course == 2:
            b = {'student cipher': cipher_counter,
                 'date': '20.12.22',
                 'subject cipher': 3100,
                 'mark': random.choice([0, 1, 1, 1, 1])
                 }
            zachet.append(b)
            b = {'student cipher': cipher_counter,
                 'date': '22.12.22',
                 'subject cipher': 3101,
                 'mark': random.choice([0, 1, 1, 1, 1])
                 }
            zachet.append(b)
            b = {'student cipher': cipher_counter,
                 'date': '24.12.22',
                 'subject cipher': 3102,
                 'mark': random.choice([0, 1, 1, 1, 1])
                 }
            zachet.append(b)
            b = {'student cipher': cipher_counter,
                 'date': '26.12.22',
                 'subject cipher': 3103,
                 'mark': random.choice([0, 1, 1, 1, 1])
                 }
            zachet.append(b)
        cipher_counter += 1


'''generate(group1_1, 1, 'КРМО-01-22')  # генерирует списки групп
generate(group1_2, 1, 'КРМО-02-22')
generate(group2_1, 2, 'КРМО-01-21')
generate(group2_2, 2, 'КРМО-02-21')'''

for i in range(len(zachet)):
    print(zachet[i])
