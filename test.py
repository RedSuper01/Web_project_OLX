from requests import get, post, delete

print(delete('http://localhost:5000/api/v2/users/999').json())
print(delete('http://localhost:5000/api/v2/users/10').json())