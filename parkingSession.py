from datetime import datetime

class ParkingSession:
    def __init__(self, entry_date: datetime, car_number: str, ticket_number: int):
        self.ticket_number = ticket_number
        self.entry_date = entry_date
        self.car_number = car_number
        self.payment_date = None
        self.exit_date = None
        self.total_payment = 0
        self.user = None