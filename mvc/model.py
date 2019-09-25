

listOfCars = [{"modelName":"BWM", "year": 2000, "name": "BMW noob", "brand": "Google"},
    {"modelName":"BWM", "year": 2000, "name": "BMW noob", "brand": "Google"},
    {"modelName":"askfasf", "year": 643643, "name": "BMW noob", "brand": "Google"},
    {"modelName":"Jesper", "year": 643643, "name": "BMW noob", "brand": "Google"},
    {"modelName":"BWM", "year": 2000, "name": "BMW noob", "brand": "Google"},
    {"modelName":"Google", "year": 36, "name": "BMW noob", "brand": "Google"},
    {"modelName":"BWM", "year": 2000, "name": "BMW noob", "brand": "Google"},
    {"modelName":"Facebook", "year": 36, "name": "BMW noob", "brand": "Google"},
    {"modelName":"BWM", "year": 2000, "name": "BMW noob", "brand": "Google"},
    {"modelName":"Min hjemmeside", "year": 2000, "name": "BMW noob", "brand": "Google"},
    {"modelName":"BWM", "year": 643643, "name": "BMW noob", "brand": "Google"},
    {"modelName":"Hahhaa", "year": 2000, "name": "BMW noob", "brand": "Google"},
    {"modelName":"BWM", "year": 63463, "name": "BMW noob", "brand": "Google"},
    {"modelName":"Hehehe", "year": 2000, "name": "BMW noob", "brand": "Google"},
    {"modelName":"BW TEST M", "year": 2015, "name": "BMW TEST", "brand": "Facebook"}]


class Car(object):
    def __init__(self, modelName = None, year = None, name = None, brand = None):
        self.modelName = modelName
        self.year = year
        self.name = name
        self.brand = brand
    
    def carInfo(self):
        return ("%s %i %s %s" % (self.modelName, self.year, self.name, self.brand))

    @classmethod
    def getAllCars(self):
        result = []

        for item in listOfCars:
            car = Car(item["modelName"], item["year"], item["name"], item["brand"])
            result.append(car)
        
        return result