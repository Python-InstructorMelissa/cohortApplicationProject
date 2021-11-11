from app.config.mysqlconnection import connectToMySQL

class Employee:
    db_name = "park_schema"
    r = connectToMySQL(db_name).query_db
    def __init__(self, data):
        self.id = data['id']
        self.eFirstName = data['eFirstName']
        self.eLastName = data['eLastName']
        self.eEmail = data['eEmail']
        self.job = []
        self.address = []
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM employees;"
        # results_from_db = cls.r(query)
        results_from_db = connectToMySQL(cls.db_name).query_db(query)
        
        allEmployees = []
        for row in results_from_db:
            e = cls(row)
            allEmployees.append(e)
        return allEmployees

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM employees WHERE id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        print("Get one Worker: ", result)
        return cls(result[0])

    @classmethod
    def getJob(cls, data):
        query = "SELECT * FROM employees LEFT JOIN parks on parks.id = employees.parks_id WHERE employees.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # print("Get Job results: ", results)
        j = cls(results[0])
        # print("job before: ", j.job)
        for row in results:
            theJ = {
                'parkName': row['parkName']
            }
            # print("print theJ: ", theJ)
            j.job.append((theJ))
            # print("job after: ", j.job)
        # print("printing job: ", j.job)
        return j.job

    @classmethod
    def save(cls, data):
        query = "INSERT INTO employees (eFirstname, eLastName, eEmail, parks_id) VALUES (%(eFirstName)s, %(eLastName)s, %(eEmail)s, %(parks_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE employees SET eFirstName=%(eFirstName)s, eLastName=%(eLastName)s, eEmail=%(eEmail)s, parks_id=%(parks_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM employees WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def getAddress(cls, data):
        query = "SELECT * FROM employees LEFT JOIN employeeAddress on employees.id = employees_id WHERE employees.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # print("Get Job results: ", results)
        e = cls(results[0])
        # print("job before: ", j.job)
        for row in results:
            theA = {
                'eStreet': row['eStreet'],
                'eCity': row['eCity'],
                'eState': row['eState'],
                'eZip': row['eZip'],
                'employees_id': row['employees_id']
            }
            # print("print theJ: ", theJ)
            e.address.append((theA))
            # print("job after: ", j.job)
        # print("printing job: ", j.job)
        return e.address