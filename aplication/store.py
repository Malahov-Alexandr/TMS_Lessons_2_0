from flask import Flask, render_template

from aplication.database.products import Product

app = Flask(__name__)

# Static file route for the home page
@app.route('/')
def base_page():
    return app.send_static_file('home_page.html')

# Route for the home page (non-static)
@app.route('/home_page')
def home_page():
    return 'You are on the Home page'

# Route for the catalog page
@app.route('/catalogue')
def catalogue_page():
    # Assuming Product is correctly imported and configured
    products = Product.objects.all()
    return render_template('catalog.html', products=products)

# Route for the detail page
@app.route('/catalogue/detail')
def detail_page():
    return 'You are on the Detail page of an item'

# Route for the card page
@app.route('/card')
def card_page():
    return 'You are on the Card page '

# Route for the personal area page
@app.route('/personal_area')
def personal_area_page():
    return 'You are on the Personal area'

if __name__ == '__main__':
    app.run()
