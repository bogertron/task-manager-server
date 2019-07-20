from taskmanager.context import db
from taskmanager.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class UserDataService:

    def __init__(self):
        self.__engine = db.get_engine()
        self.__Session = sessionmaker(bind=self.__engine)


    def getAllUsers(self):
        users = []
        session = self.__Session()

        for u in session.query(User):
            users.append(u)

        return users