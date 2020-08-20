formats = {'ymd': '{obj.year}/{obj.month}/{obj.day}',
           'mdy': '{obj.month}/{obj.day}/{obj.year}',
           'default': '{obj.day}.{obj.month}.{obj.year}'}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            return formats['default'].format(obj=self)
        return formats[format_spec].format(obj=self)

date = Date(2020, 8, 4)
print(format(date, 'ymd'))
print(format(date, 'mdy'))
print(format(date))



