from flask_app.config.mysqlconnection import connectToMySQL

class Items:
    db = 'dec-jan-Friday'
    def __init__(self, data):
        self.id = data['id']
        self.itemName = data['itemName']
        self.itemInfo = data['itemInfo']
        self.category_id = data['category_id']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM items;'
        results = connectToMySQL(cls.db).query_db(query)
        allItems = []
        for row in results:
            item = cls(row)
            allItems.append(item)
        return allItems

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM items WHERE id = %(id)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO items (itemName, itemInfo, category_id, user_id) VALUES (%(itemName)s, %(itemInfo)s, %(category_id)s, %(user_id)s);'
        print("items from query save", query)
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE items SET itemName=%(itemName)s, itemInfo=%(itemInfo)s, category_id=%(category_id)s, user_id=%(user_id)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM items WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def itemsLists(cls, data):
        # select * from items left join list on item.id
        pass
    