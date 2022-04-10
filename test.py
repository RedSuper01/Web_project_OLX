from requests import post, delete

print(delete('http://localhost:5000/api/v2/goods/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/v2/goods/1').json())
