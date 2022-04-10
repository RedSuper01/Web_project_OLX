from flask import Flask, jsonify, render_template
from flask import abort, redirect, request, make_response
from data import db_session, goods_api
from data.users import User
from data.goods import Goods
from forms.user import RegisterForm
from flask_login import login_required, LoginManager, login_user, logout_user, current_user
from forms.login import LoginForm
from forms.profile import ProfileForm
from forms.goods import GoodsForm
from flask_restful import abort, Api
import goods_resources
import users_resources

app = Flask(__name__)
api = Api(app)
# для списка объектов
api.add_resource(goods_resources.GoodsListResource, '/api/v2/goods')

# для одного объекта
api.add_resource(goods_resources.GoodsResource, '/api/v2/goods/<int:goods_id>')

api.add_resource(users_resources.UsersListResource, '/api/v2/users')

# для одного объекта
api.add_resource(users_resources.UserResource, '/api/v2/users/<int:user_id>')
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/goods_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def goods_delete(id):
    db_sess = db_session.create_session()
    goods = db_sess.query(Goods).filter(Goods.id == id,
                                      Goods.user == current_user).first()
    if goods:
        db_sess.delete(goods)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')



@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_user():
    form = ProfileForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        if user:
            form.name.data = user.name
            form.surname.data = user.surname
            form.age.data = user.age
            form.contacts.data = user.contacts
            form.email.data = user.email
            form.photo.data = user.photo
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        if user:
            user.name = form.name.data
            user.surname = form.surname.data
            user.age = form.age.data
            user.contacts = form.contacts.data
            user.email = form.email.data
            user.photo = form.photo.data
            db_sess.commit()
            return redirect('/profile')
        else:
            abort(404)
    return render_template('profile_edit.html',
                           title='Редактирование товара',
                           form=form)



@app.route('/goods/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_goods(id):
    form = GoodsForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        goods = db_sess.query(Goods).filter(Goods.id == id, Goods.user == current_user).first()
        if goods:
            form.good.data = goods.good
            form.price.data = goods.price
            form.description.data = goods.description
            form.photo.data = goods.photo
            form.contacts.data = goods.contacts
            form.is_sold = goods.is_sold
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        goods = db_sess.query(Goods).filter(Goods.id == id,
                                          Goods.user == current_user).first()
        if goods:
            goods.good = form.good.data
            goods.price = form.price.data
            goods.description = form.description.data
            goods.photo = form.photo.data
            goods.contacts = form.contacts.data
            goods.is_sold = form.is_sold.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('goods.html',
                           title='Редактирование товара',
                           form=form)


@app.route('/goods', methods=['GET', 'POST'])
@login_required
def add_goods():
    form = GoodsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        goods = Goods()
        goods.good = form.good.data
        goods.price = form.price.data
        goods.description = form.description.data
        goods.photo = form.photo.data
        goods.contacts = form.contacts.data
        goods.is_sold = form.is_sold.data
        current_user.goods.append(goods)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('goods.html', title='Добавление товара',
                           form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template("login.html",
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизция', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            contacts=form.contacts.data,
            email=form.email.data,
            photo=form.photo.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/')
@app.route('/main')
def main():
    db_sess = db_session.create_session()
    goods = db_sess.query(Goods)
    return render_template("index.html", goods=goods)


@app.route('/profile')
def about_me():
    return render_template("profile.html")


@app.route('/good/<int:id>')
def good_page(id):
    db_sess = db_session.create_session()
    good = db_sess.query(Goods).filter(Goods.id == id).first()
    print(good)
    return render_template("goods_page.html", good=good)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/help')
def help():
    return render_template("help.html")


@app.route('/something')
def something():
    return render_template("base.html")

if __name__ == '__main__':
    db_session.global_init("db/MY_OLX.db")


    db_sess = db_session.create_session()

    app.register_blueprint(goods_api.blueprint)
    print(current_user)
    if current_user:
        if current_user.is_authenticated:
            goods = db_sess.query(Goods).filter(
                Goods.user == current_user)
        else:
            goods = db_sess.query(Goods)

    app.run()

