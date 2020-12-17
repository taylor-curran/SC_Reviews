from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .api import df
import pandas as pd
import numpy as np

# A home route that displays at least one entry from a 
# database of stored BGG game information

# A dynamic route /add/<game_id> that adds game information 
# into your database based on the ID in the route.

# A route that resets the database

#The database should have the following following columns as 
# a minimum: id (integer), name (string), and max_players (integer)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# -- Define Tables --

db = SQLAlchemy(app)

class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    min_max_players = db.Column(db.String(200))
    playing_time = db.Column(db.Float)
    description = db.Column(db.String(600))
    game_mechanics = db.Column(db.String(200))

    def __init__(self, game_id, name, min_max_players, playing_time, description, game_mechanics):
        self.game_id = game_id
        self.name = name
        self.min_max_players = min_max_players
        self.playing_time = playing_time
        self.description = description
        self.game_mechanics = game_mechanics

    def __repr__self(self):
        return '<Game %r>' % self.name

# To Use the Tables Defined in the DB as Above,
# Run the creat_all() method on the db object


# Populate DB
# for index in n_rows in df
for i in range(df.shape[1]):
    df_row = df.iloc[i]
    alch_row = Game(game_id=int(df_row[0]), 
                    name=str(df_row[1]), 
                    min_max_players=str(df_row[2]), 
                    playing_time=float(df_row[3]), 
                    description=str(df_row[4]), 
                    game_mechanics=str(df_row[5]))
    db.session.add(alch_row)
db.session.commit()

@app.route("/")
def hello_world():
    return 'Hello World!'

@app.route("/reset")
def reset():
    DB.drop_all()
    DB.create_all()
    return "Reset Complete"

