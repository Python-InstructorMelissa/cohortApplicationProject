from flask_app.config.mysqlconnection import connectToMySQL

class Category:
    db = 'dec-jan-Friday'
    def __init__(self, data):
        self.id = data['id']
        self.categoryName = data['categoryName']
        self.categoryInfo = data['categoryInfo']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM category;'
        results = connectToMySQL(cls.db).query_db(query)
        allCats = []
        for row in results:
            category = cls(row)
            allCats.append(category)
        return allCats

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM category WHERE id = %(id)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO category (categoryName, categoryInfo) VALUES (%(categoryName)s, %(categoryInfo)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE category SET categoryName=%(categoryName)s, categoryInfo=%(categoryInfo)s, user_id=%(user_id)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM category WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def catItems(cls, data):
        # select all from cat left join items on cat id
        pass