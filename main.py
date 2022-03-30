from flask import Flask, render_template
from header_pages import about_me, contacts, help

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")


@app.route('/about_me')
def about_me():
    return render_template("about_me.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/help')
def help():
    return render_template("help.html")


@app.route('/something')
def something():
    return render_template("base_header.html")

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
