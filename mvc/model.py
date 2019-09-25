

listOfCars = [{"modelName":"BWM", "year": 2000, "name": "BMW noob", "brand": "Google"},
    {"modelName":"BW TEST M", "year": 2015, "name": "BMW TEST", "brand": "Facebook"}]


class Car(object):
    def __init__(self, modelName = None, year = None, name = None, brand = None):
        self.modelName = modelName
        self.year = year
        self.name = name
        self.brand = brand
    
    def carInfo(self):
        return ("%s %i %s" % (self.modelName, self.year, self.name))

    @classmethod
    def getAllCars(self):
        result = []

        for item in listOfCars:
            car = Car(item["modelName"], item["year"], item["name"], item["brand"])
            result.append(car)
        
        return result