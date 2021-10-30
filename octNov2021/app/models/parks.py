from app.config.mysqlconnection import connectToMySQL

class Park:
    db_name = "park_schema"
    r = connectToMySQL(db_name).query_db
    def __init__(self, data):
        self.id = data['id']
        self.parkName = data['parkName']
        self.parkDesc = data['parkDesc']
        self.parkLocation = data['parkLocation']
        self.parkType = data['parkType']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM parks;"
        # results_from_db = cls.r(query)
        results_from_db = connectToMySQL(cls.db_name).query_db(query)
        
        allParks = []
        for row in results_from_db:
            park = cls(row)
            allParks.append(park)
        return allParks

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM parks WHERE id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO parks (parkName, parkDesc, parkLocation, parkType) VALUES (%(parkName)s, %(parkDesc)s, %(parkLocation)s, %(parkType)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE parks SET parkName=%(parkName)s, parkDesc=%(parkDesc)s, parkLocation=%(parkLocation)s, parkType=%(parkType)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM parks WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)