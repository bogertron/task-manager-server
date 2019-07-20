import json
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def loadConfig(fileName):
    with open(fileName) as json_data_file:
        data = json.load(json_data_file)
    repository = data["repository"]
    dbUrl = "postgres://{0}:{1}@{2}:{3}/{4}".format(repository["user"], repository["password"], 
        repository["host"], repository["port"], repository["schema"])
    return dbUrl

app = Flask(__name__)
cfg = loadConfig(os.getcwd() + "/conf/config.json")
app.config["SQLALCHEMY_DATABASE_URI"] = cfg
db = SQLAlchemy(app)