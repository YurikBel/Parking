from parkingManager import *
from tariffLoader import *
from datetime import datetime

tariff_loader = TariffMemoryLoader()
capacity = 50
parking_manager = ParkingManager(capacity, tariff_loader)
parking_manager.fill_users()
car = parking_manager.enter_parking(839)
car2 = parking_manager.enter_parking(838)
car2.entry_date = datetime.strptime('2020-04-25 11:02:26', '%Y-%m-%d %H:%M:%S')
car.entry_date = datetime.strptime('2021-12-21 23:02:26', '%Y-%m-%d %H:%M:%S')
parking_manager.GetRemainingCost(1)
parking_manager.GetRemainingCost(2)


print(parking_manager.users[0].car_number)
print(parking_manager.users[0].money)
print(car2.user)
print(car.total_payment)
print(car.ticket_number)
parking_manager.PayForParking(1)
parking_manager.TryLeaveParkingByCarPlateNumber(838)
if parking_manager.Try_leave_parking(1):
    print('Вы покинули парковку')
else:
    print('Вам надо оплатить парковку')
print(parking_manager.users[0].money)