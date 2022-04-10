from data import db_session
from data.goods import Goods
from data.reqparse import parser
from flask import jsonify, abort
from flask_restful import abort, Resource


def abort_if_news_not_found(goods_id):
    session = db_session.create_session()
    goods = session.query(Goods).get(goods_id)
    if not goods:
        abort(404, message=f'Goods {goods_id} not found')


class GoodsResource(Resource):
    def get(self, goods_id):
        abort_if_news_not_found(goods_id)
        session = db_session.create_session()
        goods = session.query(Goods).get(goods_id)
        return jsonify({'goods': goods.to_dict(
            only=('good', 'price', 'description', 'contacts')
        )})

    def delete(self, goods_id):
        abort_if_news_not_found(goods_id)
        session = db_session.create_session()
        goods = session.query(Goods).get(goods_id)
        session.delete(goods)
        session.commit()
        return jsonify({'success': 'OK'})


class GoodsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        goods = session.query(Goods).all()
        return jsonify({'goods': [item.to_dict(only=('good', 'price', 'description', 'contacts')) for item in goods]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        goods = Goods(
            good=args['good'],
            price=args['price'],
            description=args['description'],
            contacts=args['contacts']
        )
        session.add(goods)
        session.commit()
        return jsonify({'success': 'OK'})
