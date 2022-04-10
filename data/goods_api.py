import flask
from flask import jsonify, request
from . import db_session
from .goods import Goods


blueprint = flask.Blueprint(
    'good_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/goods')
def get_goods():
    db_sess = db_session.create_session()
    goods = db_sess.query(Goods).all()
    return jsonify(
        {
            "goods":
                [item.to_dict(only=('good', 'price', 'description', 'contacts', 'user.name'))
                 for item in goods]
        }
    )


@blueprint.route('/api/goods/<int:goods_id>', methods=['GET'])
def get_one_goods(goods_id):
    db_sess = db_session.create_session()
    goods = db_sess.query(Goods).get(goods_id)
    if not goods:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'goods': goods.to_dict(only=('good', 'price', 'description', 'contacts', 'user_id'))
        }
    )


@blueprint.route('/api/goods', methods=['POST'])
def create_goods():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['good', 'price', 'description', 'contacts', 'user_id']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    goods = Goods(
        good=request.json['good'],
        price=request.json['price'],
        description=request.json['description'],
        contacts=request.json['contacts'],
        user_id=request.json['user_id']
    )
    db_sess.add(goods)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/goods/<int:goods_id>', methods=['DELETE'])
def delete_goods(goods_id):
    db_sess = db_session.create_session()
    goods = db_sess.query(Goods).get(goods_id)
    if not goods:
        return jsonify({'error': 'Not found'})
    db_sess.delete(goods)
    db_sess.commit()
    return jsonify({'success': 'OK'})