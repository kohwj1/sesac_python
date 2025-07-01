from driver import Driver
from car import Car

driver = Driver('Bob',40,'1종보통')
driver.drive(30)

mycar = Car('tesla','model s')
driver.assign_car(mycar)

driver.drive(50)
driver.drive(60)

mycar.update_odometer(100)
mycar.update_odometer(200)
mycar.read_odometer()