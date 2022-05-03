from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(200))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.user_name,
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    birth_year = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    height = db.Column(db.String(250))
    mass = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    model = db.Column(db.String(250))
    vehicle_class = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    length = db.Column(db.String(250))
    cost_in_credits = db.Column(db.String(250))
    crew = db.Column(db.String(250))
    passengers = db.Column(db.String(250))
    max_atmosphering_speed = db.Column(db.String(250))
    cargo_capacity = db.Column(db.String(250))
    consumables = db.Column(db.String(250))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "length": self.length,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables
            
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)      
    name = db.Column(db.String(250), nullable=False, unique=True)
    diameter = db.Column(db.String(250))
    rotation_period = db.Column(db.String(250))
    orbital_period = db.Column(db.String(250))
    gravity = db.Column(db.String(250))
    population = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.String(250))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship(Character)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    vehicle = db.relationship(Vehicle)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id')) 
    planet = db.relationship(Planet)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "character_id": self.character_id,
            "vehicle_id": self.vehicle_id,
            "planet_id": self.planet_id
        }