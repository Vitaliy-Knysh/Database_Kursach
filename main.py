# --------------------------------------------------------------------------------------------------------------------
# нужно сделать запросы:
# -вывести конкретные оценки по предмету, все оценки по предмету, оценки группы √
# -вывести то же самое для зачётов √
# -добавить студента в базу, исключить студента из базы
# -добавить предмет в базу, исключить предмет из базы
# -изменить оценку студента(дополнительно?)
# ДОПОЛНИТЕЛЬНО: сделать единый шаблон запроса для зачётов и экзаменов, а в функции менять только нужные поля
# --------------------------------------------------------------------------------------------------------------------

from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=["http://localhost:9200"])


def mark_query(group_number, subject_sipher, marks_to_print):  # запрос на список студентов с конкретными оценками
                                                                # (оценкой)
    gte = 1000 + ((group_number - 1) * 20)  # с этого числа начинается отсчёт студентов группы
    lte = 999 + (group_number * 20)  # с этого числа заканчивается отсчёт студентов группы
    body = {
        "from": 0,
        "size": 20,
        "query": {
            "bool": {
                "must": [
                    {"terms": {"mark": marks_to_print}},  # требуемые оценки, любой набор от 2 до 5
                    {"match": {"subject cipher": subject_sipher}},  # шифр предмета
                    {"range": {"student cipher": {"gte": gte, "lte": lte}}}  # шифр студентов конкретной группы
                ]
            }
        }
    }
    return es.search(index="exams", body=body)

def zachet_query(group_number, subject_sipher, marks_to_print):
    gte = 1000 + ((group_number - 1) * 20)  # с этого числа начинается отсчёт студентов группы
    lte = 999 + (group_number * 20)  # с этого числа заканчивается отсчёт студентов группы
    body = {
        "from": 0,
        "size": 20,
        "query": {
            "bool": {
                "must": [
                    {"terms": {"mark": marks_to_print}},  # требуемые оценки
                    {"match": {"subject cipher": subject_sipher}},  # шифр предмета
                    {"range": {"student cipher": {"gte": gte, "lte": lte}}}  # шифр студентов конкретной группы
                ]
            }
        }
    }
    return es.search(index="zachet", body=body)


if __name__ == '__main__':
    res = zachet_query(1, 3000, [0])
    for i in range(len(res["hits"]["hits"])):
        print(i, ": ", res["hits"]["hits"][i]["_source"])
