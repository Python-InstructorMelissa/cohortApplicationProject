from app.config.mysqlconnection import connectToMySQL
from .employees import Employee

class EmployAddress:
    db_name = "park_schema"
    def __init__(self, data):
        self.id = data['id']
        self.eStreet = data['eStreet']
        self.eCity = data['eCity']
        self.eState = data['eState']
        self.eZip = data['eZip']
        self.createAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM employeeAddress WHERE id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO employeeAddress (eStreet, eCity, eState, eZip, employees_id) VALUES (%(eStreet)s, %(eCity)s, %(eState)s, %(eZip)s, %(employees_id)s);'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE employeeAddress SET eStreet=%(eStreet)s, eCity=%(eCity)s, eState=%(eState)s, eZip=%(eZip)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM employeeAddress WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)