class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def display(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

    def __add__(self, other):
        if isinstance(other, Time):
            total_seconds = self.__second + other.__second
            total_minutes = self.__minute + other.__minute + total_seconds // 60
            total_hours = self.__hour + other.__hour + total_minutes // 60

            new_second = total_seconds % 60
            new_minute = total_minutes % 60
            new_hour = total_hours % 24 

            return Time(new_hour, new_minute, new_second)
        else:
            raise TypeError("Operands must be of type Time")


time1 = Time(2, 45, 50)
time2 = Time(1, 20, 15)

sum_time = time1 + time2
print("Time 1:", time1.display())
print("Time 2:", time2.display())
print("Sum:", sum_time.display())
