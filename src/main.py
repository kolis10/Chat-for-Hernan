"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import seeds
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Users, Chats
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/seeds', methods=[ 'GET']) #clean tables
def seed(): 
    return seeds.run()


@app.route('/users', methods=['POST']) #register
def handle_register():

    json = request.get_json()

    property_check = ['username']
    missing_props = []
    empty_props = []
    for prop in property_check:
        if prop not in json:
            missing_props.append(prop)
    if len(missing_props) > 0:
        raise APIException(f'Missing {", ".join(missing_props)} property in json')

    for prop in property_check:
        if json[prop] == "":
            empty_props.append(prop)
    if len(empty_props) > 0:
        raise APIException(f'Missing {", ".join(empty_props)} data in json')

    db.session.add(Users(
        username = json['username']
    ))
    db.session.commit()
    return jsonify(json)

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
