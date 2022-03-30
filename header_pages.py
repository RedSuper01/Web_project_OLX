from flask import Flask, render_template, url_for

app = Flask(__name__)

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
    return "Что-нибудь"