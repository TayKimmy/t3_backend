""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# Define the Time class to manage actions in the 'times' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Time represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Time(db.Model):
    __tablename__ = 'times'  # table name is plural, class name is singular

    # Define the Time schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=False, nullable=False)   
    _totaltime = db.Column(db.Float, unique=False, nullable=False)
 

    # constructor of a Time object, initializes the instance variables within object (self)
    def __init__(self, totaltime, uid):
        self._uid = uid
        self._totaltime = totaltime

    # a getter method, extracts totaltime from object
    @property
    def totaltime(self):
        return self._totaltime
    
    # a setter function, allows name to be updated after initial object creation
    @totaltime.setter
    def totaltime(self, totaltime):
        self._totaltime = totaltime              
    
    # a getter method, extracts uid from object
    @property
    def uid(self):
        return self._uid
    
    # a setter function, allows name to be updated after initial object creation
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, uid):
        return self._uid == uid
    
  
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a timeer object from Time(db.Model) class, passes initializers
            print("Inside create")
            print(id,self.uid,self.totaltime)
            db.session.add(self)  # add prepares to persist person object to Times table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # read converts self to dictionary
    # returns dictionary
    def read(self):
        # entry = db.session.query(Times).get(args["id"])
        # print(id,self.uid,self.totaltime)
        return {
            "id": self.id,
            "totaltime":self.totaltime,
            "uid": self.uid            
        }
    
    def delete(id):
        # print("inside reviews.py delete", id) 
        try:
            entry = db.session.query(Time).get(id)
            if entry: 
                db.session.delete(entry)
                db.session.commit()
                print("deleted record", entry)                
                return None
            else:
                return {"error": "entry not found"}, 404                
        except Exception as e:
            db.session.rollback()
            return {"error": f"server error: {e}"}, 500

# Builds working data for testing
def initTimes():
    with app.app_context():
        """Create database and tables"""
        # db.init_app(app)
        db.create_all()
        """Tester data for table"""
        u1 = Time(uid='toby', totaltime=5)
        u2 = Time(uid='niko', totaltime=6.985)
        u3 = Time(uid='lex', totaltime=3.61)
        u4 = Time(uid='whit', totaltime=8.124)
        u5 = Time(uid='jm1021', totaltime=10.2)

        times = [u1, u2, u3, u4, u5]

        """Builds sample time/comment(s) data"""
        for time in times:
            try:
                time.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {time.uid}")


