from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app.models import item

class User:
    db = 'dec-jan-Friday'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        # this is needed for the join of the users Items
        self.itemList = []

    @staticmethod
    def validate(user):
        isValid = True
        q = 'SELECT * FROM user WHERE email = %(email)s;'
        r = connectToMySQL(User.db).query_db(q, user)
        if len(r) >= 1:
            isValid = False
            flash("That email is already registered!")
        if len(user['password']) < 6:
            isValid = False
            flash("Password must be at least 6 characters long")
        if len(user['firstName']) < 2:
            isValid = False 
            flash("First name must be at least 2 characters long")
        if len(user['lastName']) < 2:
            isValid = False 
            flash("Last name must be at least 2 characters long")
        if not EMAIL_REGEX.match(user['email']):
            isValid = False
            flash("Please us a proper email")
        if user['password'] != user['confirm']:
            isValid = False
            flash("Your Passwords don't match")

        return isValid

    @classmethod
    def getAll(cls):
        q = 'SELECT * FROM user;'
        r = connectToMySQL(cls.db).query_db(q)
        users = []
        for user in r:
            users.append(cls(user))
        return users

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getEmail(cls, data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        q = 'INSERT INTO user (firstName, lastName, email, password) VALUES (%(firstName)s, %(lastName)s, %(email)s, %(password)s);'
        return connectToMySQL(cls.db).query_db(q, data)

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass

# This is the join for the Users items
    @classmethod
    def userItems(cls, data):
        q = 'SELECT * FROM user LEFT JOIN items ON items.user_id = user.id WHERE user.id = %(id)s;'
        r = connectToMySQL(cls.db).query_db(q, data)
        print("User Items query results: ", r)
        listing = cls(r[0])
        for row in r:
            data = {
                'id': row['items.id'],
                'itemName': row['itemName'],
                'itemInfo': row['itemInfo'],
                'category_id': row['category_id'],
                'user_id': row['user_id']
            }
            thing = item.Items(data)
            print("Each item: ", thing)
            listing.itemList.append(thing)
        return listing