from flask import Flask

app = Flask(__name__)


@app.route('/')
def base_page():
    return app.send_static_file('home_page.html')

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


if __name__ == '__main__':
    app.run()