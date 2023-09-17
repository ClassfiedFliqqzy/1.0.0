from googlesearch import search

def search_wikipedia(query):
    # Используем параметр site: для ограничения поиска только на сайте Википедии
    query += " site:wikipedia.org"

    # Выполняем поиск в Google
    results = search(query, num_results=1, advanced=True)

    # Получаем первый результат
    first_result = next(results, None)

    return first_result

# Пример использования
query = "Python (язык программирования)"
result = search_wikipedia(query)
print(result)