import datetime

class Date:
    def __init__(self, day=0, month=0, year=0):
        if type(day) == int :
            self.day = day
            self.month = month
            self.year = year
        if type(day) == str :
            self.from_string(day)

    def is_date_valid(self):
        try:
            datetime.date(self.year, self.month, self.day)
            return True
        except ValueError:
            return False

    def from_string(self, string):
       self.day = datetime.datetime.strptime(string, '%d-%M-%Y').day
       self.month = datetime.datetime.strptime(string, '%d-%M-%Y').month
       self.year = datetime.datetime.strptime(string, '%d-%M-%Y').year

    def __str__(self):
        return f'Day = {self.day}, Month = {self.month}, Year = {self.year}'

class UserDate(Date):
    pass

d1 = Date(12, 12, 2020)
print(d1.is_date_valid())
d2 = Date('01-03-2020')
d3 = UserDate(31, 12, 2020)
d4 = UserDate('14-04-2020')
print(d1)
print(d2)
print(d3)
print(d4)
print(isinstance(d2, UserDate))
