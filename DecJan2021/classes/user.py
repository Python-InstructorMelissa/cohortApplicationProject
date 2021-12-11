# removeItem =  deleting from list

class User:
    allUsers = []
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.list = [] # Setting this equal to a empty list allows us to have a place ready to store our inventory with out needing it upon user creation
        User.allUsers.append(self)

    def addItems(self, item):
        self.list.append(item)
        return self
# return allows us to have the data from this function used in or called later in another function

    def removeItem(self, item):
        for l in self.list:
            if item == l:
                # print(l.itemName)
                self.list.remove(l)
        print(f"{item.itemName} was removed from {self.firstName}'s list")
        return self

    def displayList(self):
        myList = []
        for l in self.list:
            myList.append(l.itemName)
        print(f"{self.firstName}'s Inventory: {myList}")
        return self

    def printUser(self):
        print(f"{self.firstName} {self.lastName}")
        return f"{self.firstName} {self.lastName}"

    @classmethod
    def printUsers(cls):
        for l in cls.allUsers:
            l.printUser()
    
    def updateUserFirstName(self, firstName):
        self.firstName = firstName
        return self