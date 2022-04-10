from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('good', required=True)
parser.add_argument('price', required=True)
parser.add_argument('description', required=True)
parser.add_argument('contacts', required=True)