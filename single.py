from datetime import datetime


class Singleton(object):
    __current_date = None

    @property
    def currentDate(self):
        if self.__current_date is not None:
            return self.__current_date
        else:
            return datetime.now()

    @currentDate.setter
    def currentDate(self, value):
        self.__current_date = value

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

