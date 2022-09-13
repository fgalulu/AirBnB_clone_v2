#!/usr/bin/python3
"""
Contains the class DBStorage
"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessiomaker

classes = {"Amenity": Amenity, "City": City, "Place": Place,
        "Review": Review, "State": State, "User": User}

class DBStorage:
    """Interactes with the MySQL database"""
    _engine = None
    _session = None

    def __init__(self):
        """Instantiate the DBStorage class"""
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")
        self._engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                     format(HBNB_MYSQL_USER, 
                                            HBNB_MYSQL_PWD,
                                            HBNB_MYSQL_HOST,
                                            HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self._engine)

    def all(self, cls=None):
        """query on the current db session"""
        new_dict ={}
        for cls_ in classes:
            if cls is None or cls is classes[cls_] or cls is cls_:
                objs = self._session.query(classes[cls_]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current db session"""
        self._session.add(obj)

    def save(self):
        """commit all changes of current db session"""
        self._session.commit()

    def delete(self, obj=None):
        """delete from current db session"""
        of obj is not None:
            self._session.delete(obj)

    def reload(self):
    """reload data from the db"""
        Base.metadata.create_all(self._engine)
        sess_factory = sessionmaker(bind=self._engine, expire_on_commit=False)
        Session = scope_session(sess_factory)
        self._session = Session

