from flask_restful import reqparse

# Добавляю аргументы для пользователей
parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('age', required=True)
parser.add_argument('email', required=True)
parser.add_argument('contacts', required=True)
parser.add_argument('hashed_password', required=True)
