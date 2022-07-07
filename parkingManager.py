from tariff import *
from parkingSession import *
from tariffLoader import *
from datetime import datetime
from User import *
from single import *


class ParkingManager:
    def __init__(self, capacity, tariff_loader: TariffLoader):
        self.capacity = capacity
        self.active_sessions = []
        self.close_sessions = []
        self.tariff_list = tariff_loader.load_tariffes()
        self.users = []

    def fill_users(self):
        with open('uers.txt', encoding='utf8') as f:
            lines = f.read().splitlines()
        for line in lines:
            name, car_number, money = line.split()
            user = User(name, car_number, int(money))
            self.users.append(user)

    def check_car_number(self, car_number):
        user = None
        n = self.users
        for k in self.users:
            if k.car_number == car_number:
                user = k
        return user

    @property
    def free_places(self):
        return self.capacity - len(self.active_sessions)

    def find_session(self, car_number):
        return next((s for s in self.active_sessions if s.car_number == car_number), None)

    def next_ticket_number(self):
        if len(self.active_sessions) == 0:
            return 1
        return max(s.ticket_number for s in self.active_sessions) + 1

    def enter_parking(self, car_number):
        if self.free_places == 0:
            return None
        if self.find_session(car_number) is not None:
            raise ValueError(f'Автомобиль с номером {car_number} уже стоит на парковке')
        ticket_number = self.next_ticket_number()
        session = ParkingSession(Singleton().currentDate, car_number, ticket_number)
        user = self.check_car_number(car_number)
        if user is not None:
            session.user = user
        self.active_sessions.append(session)
        return session

    def check_leave(self, session):
        now = Singleton().currentDate
        free_time = self.tariff_list[0].minutes
        if session.payment_date is None:
            delta = now - session.entry_date
        else:
            delta = now - session.payment_date
        if delta.total_seconds() / 60 < free_time:
            session.exit_date = now
            self.active_sessions.remove(session)
            self.close_sessions.append(session)
            return True
        return False

    def Try_leave_parking(self, ticket_number):
        session = next((s for s in self.active_sessions if s.ticket_number == ticket_number), None)
        return self.check_leave(session)

    def GetRemainingCost(self, ticket_number):
        now = Singleton().currentDate
        session = next((s for s in self.active_sessions if s.ticket_number == ticket_number), None)
        if session.payment_date is not None:
            delta = now - session.payment_date
        else:
            delta = now - session.entry_date
        select_tarif = self.tariff_list[-1]
        for tarif in self.tariff_list:
            if tarif.minutes >= delta.total_seconds() / 60:
                select_tarif = tarif
                break
        return select_tarif.rate

    def PayForParking(self, ticket_number, money):
        session = next((s for s in self.active_sessions if s.ticket_number == ticket_number), None)
        session.total_payment = money
        now = Singleton().currentDate
        session.payment_date = now

    def TryLeaveParkingByCarPlateNumber(self, car_number):
        session = next((s for s in self.active_sessions if s.car_number == car_number), None)
        if session.user is None:
            raise ValueError('Этот номер не зарегистрирован')
        if not self.check_leave(session):
            now = Singleton().currentDate
            session.user.money -= session.total_payment
            session.payment_date = now
            session.exit_date = now
        return True



