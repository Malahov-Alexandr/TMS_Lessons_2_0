from flask import Flask

app = Flask(__name__)


@app.route('/')
def base_page():
    return app.send_static_file('home_page.html')


@app.route('/home_page')
def home_page():
    return 'You are on the Home page'


@app.route('/catalogue')
def catalogue_page():
    return 'You are on the Catalogue page'


@app.route('/catalogue/detail')
def detail_page():
    return 'You are on the Detail page of an item'


@app.route('/card')
def card_page():
    return 'You are on the Card page '


@app.route('/personal_area')
def personal_area_page():
    return 'You are on the Personal area'


if __name__ == '__main__':
    app.run()
