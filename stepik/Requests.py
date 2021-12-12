import requests

r = requests.get("https://translate.google.com/?hl=ru")  # простой Get запрос
print(r.text)  # вывод ответа от сервера 
# ctrl+alt+l форматирование всего под стандартны PEP 8 

url = "https://example.com"
par = {'key1': 'valeu1', 'key2': 'value2'}
r = requests.get(url, params=par)  # передача параметров в запрос
print(r.url)  # сформированный юрл-адрес с учетом параметров гет-запроса

url = "http://httpbin.org/cookies"
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)  # отправка сформированных куки
# на сервер
print(r.text)

print(r.cookies['example_cookies_name'])  # использование куки, полученных от сервера
