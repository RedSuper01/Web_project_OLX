from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/about_me')
def about_me():
    return render_template("about_me.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
