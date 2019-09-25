
from model import Car

def showAllCars(list):
    print('Her er alle bil - Den er så lang: %i' % len(list))
    for item in list:
        print(item.carInfo())
        

def startView():
    print("Skal vi starte nu?")
    print("Tryk y / n?")

def endView():
    print("Farvel mark din noob!")

    
