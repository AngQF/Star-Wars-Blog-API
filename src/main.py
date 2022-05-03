"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Vehicle, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_serialized = list(map(lambda user: user.serialize(), users))
    return jsonify({"users": users_serialized}), 200

@app.route('/users/favorites', methods=['GET'])
def get_users_favorites():
    user_favorites = Favorite.query.all()
    user_fav_serialized = list(map(lambda fav: fav.serialize(), user_favorites))
    return jsonify({"user_favorites": user_fav_serialized}), 200

@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    characters_serialize = list(map(lambda character: character.serialize(), characters))
    return jsonify({"characters": characters_serialize}), 200    

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_characters_by_id(character_id):
    character = Character.query.get(character_id)
    return jsonify({"character": character.serialize()}), 200    

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    planets_serialize = list(map(lambda planet: planet.serialize(), planets))
    return jsonify({"planets": planets_serialize}), 200    

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planets_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    return jsonify({"character": planet.serialize()}), 200    

@app.route('/user/<int:user_id>/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet_by_id(planet_id,user_id):
    favorite = Favorite(user_id = user_id, planet_id = planet_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify(({'favorites': favorite.serialize()})), 200

@app.route('/user/<int:user_id>/favorite/character/<int:character_id>', methods=['POST'])
def add_favorite_character_by_id(character_id,user_id):
    favorite = Favorite(user_id = user_id, character_id = character_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify(({'favorites': favorite.serialize()})), 200

@app.route('/user/<int:user_id>/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet_by_id(planet_id,user_id):
    fav = Favorite.query.filter_by(user_id = user_id).filter_by(planet_id = planet_id).first()
    db.session.delete(fav)
    db.session.commit()
    return jsonify(({"deleted": True})), 200    

@app.route('/user/<int:user_id>/favorite/character/<int:char_id>', methods=['DELETE'])
def delete_favorite_character_by_id(char_id, user_id):
    fav = Favorite.query.filter_by(user_id = user_id).filter_by(character_id = char_id).first()
    db.session.delete(fav)
    db.session.commit()
    return jsonify({"deleted": "OK"}), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
