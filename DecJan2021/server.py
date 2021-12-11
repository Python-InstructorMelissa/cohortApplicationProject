import sys
from classes.user import User
from classes.inventory import Inventory

# print("Hello World")


# Create Users
jane = User("Jane", "Doe")
john = User("John", "Smith")

# Create Inventory
theCore = Inventory("The Core", "DVD", "Movie")
warGames = Inventory("War Games", "DVD", "Movie")
wallFlowers = Inventory("Wall Flowers", "DVD", "Movie")
ncis = Inventory("NCIS", "DVD", "TV Show")
westWing = Inventory("West Wing", "DVD", "TV Show")


# Print Users
# jane.printUser()
# john.printUser()

# Print all
# Inventory.printAllItems()
# User.printUsers()


# Add Inventory to user
jane.addItems(theCore).addItems(warGames)
john.addItems(wallFlowers).addItems(ncis).addItems(westWing)

# Print users Inventory
# jane.displayList()
# john.displayList()

# Remove Inventory from user
john.removeItem(ncis)


john.displayList()

# Update Item Name
westWing.updateItem("Supernatural")
westWing.displayItems()
john.displayList()

john.updateUserFirstName("Johnathan")
john.printUser()

if __name__ == "__main__":
    sys.exit()