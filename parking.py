import car
import time

MAX = 10
car_list=[]
if len(car_list) < MAX:
    car1 = car.Car("111가1111")
    car_list.append(car1)
    print(car1.intime)
    print(car1.outtime)
    time.sleep(2)
    number = "111가1111"
    for car in car_list:
        if car.number == number:
            car1.out()#----------------------------
            print(car1.intime)
            print(car1.outtime)
            print(car1.gettime())
            print(car1.calprice())
            break

