from flask_mongoengine import MongoEngine
from aplication.store import app

db = MongoEngine(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'shopdb',
    'host': 'localhost',
    'port': 27017,
}


class Product(db.Document):
    name = db.StringField(required=True, max_length=255)
    description = db.StringField(required=True, max_length=255)
    price = db.FloatField(required=True)  # Corrected to FloatField for price
    image_url = db.StringField(max_length=255)
