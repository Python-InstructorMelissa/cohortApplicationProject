from flask_app.config.mysqlconnection import connectToMySQL

class List:
    db = 'dec-jan-Friday'
    def __init__(self, data):
        self.id = data['id']
        self.listName = data['listName']
        self.listInfo = data['listInfo']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM list;'
        results = connectToMySQL(cls.db).query_db(query)
        allLists = []
        for row in results:
            list = cls(row)
            allLists.append(list)
        return allLists

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM list WHERE id = %(id)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO list (listName, listInfo, user_id) VALUES (%(listName)s, %(listInfo)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE list SET listName=%(listName)s, listInfo=%(listInfo)s, user_id=%(user_id)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM category WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def listItems(cls, data):
        # select * from list left join items on list.id
        pass