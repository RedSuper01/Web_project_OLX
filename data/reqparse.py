from flask_restful import reqparse

# Делаю добавляю аргументы в файле для товаров, а потом буду импортировать
parser = reqparse.RequestParser()
parser.add_argument('good', required=True)
parser.add_argument('price', required=True)
parser.add_argument('description', required=True)
parser.add_argument('contacts', required=True)
