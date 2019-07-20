from datetime import datetime
from taskmanager.context import app
import json
from taskmanager.dbservice.userservice import UserDataService

__userService = UserDataService()

@app.route("/")
def doRoot():
    return 'Start'

@app.route("/users")
def getUsers():
    users = __userService.getAllUsers();
    str = ""
    for u in users:
        str += "User: {0}\n".format(u.username)

    return str