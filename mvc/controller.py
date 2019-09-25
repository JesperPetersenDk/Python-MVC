from model import Car
import view


def showAll():
    cars = Car.getAllCars()
    return view.showAllCars(cars)


def start():
    view.startView()
    inp = input()
    if inp == "y":
        return showAll()
    else:
        return view.endView()

if __name__ == "__main__":
    start()