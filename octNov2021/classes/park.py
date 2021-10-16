class Park:
    def __init__(self, parkName, location, parkType, tickets, hours, parking):
        self.parkName = parkName
        self.location = location
        self.shops = []
        self.attractions = []
        self.parkType = parkType
        self.tickets = tickets
        self.hours = hours
        self.parking = ''
        self.animals = []
        self.plant = []
        self.employees = []

    def returnData(self):
        parks = self
        return parks

park = []


dojo=Park("Dojo Park", "Virtual", "Educational", 49.95, "24/7", "Not Required")
dojoPark = Park.returnData(dojo)

coding=Park("Dojo Zoo", "Jacksonville, FL", "Zoo", 30.50, "M-F 4pm-8pm, Saturdays 10am-8pm, Closed Sundays", "Onsite parking $5 per car")
codingPark = Park.returnData(coding)


park.append(dojoPark)
park.append(codingPark)



