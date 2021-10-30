from app.config.mysqlconnection import connectToMySQL
from .employees import Employee

class Park:
    db_name = "park_schema"
    r = connectToMySQL(db_name).query_db
    def __init__(self, data):
        self.id = data['id']
        self.parkName = data['parkName']
        self.parkDesc = data['parkDesc']
        self.parkLocation = data['parkLocation']
        self.parkType = data['parkType']
        self.workers = []
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
    def getWorkers(cls, data):
        query = "SELECT * FROM parks LEFT JOIN employees on parks.id = employees.parks_id WHERE parks.id = %(id)s ORDER BY employees.eFirstName;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # print("Get Workers: ", results)
        park =  cls(results[0])
        # print("print workers before: ", park.workers)
        for row in results:
            w = {
                'id': row['employees.id'],
                'eFirstName': row['eFirstName'],
                'eLastName': row['eLastName'],
                'eEmail': row['eEmail'],
                'createdAt': row['employees.createdAt'],
                'updatedAt': row['employees.updatedAt']
            }
            # print("print w: ", w)
            park.workers.append((w))
            # print("print workers after: ", park.workers)
        # print("Print park: ", park.workers)
        return park.workers
        

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