mins_in_days = 24*60

class Clock:
    def __init__(self, hour, minute):
        m = ((60*hour + minute)%mins_in_days + mins_in_days)%mins_in_days
        self.hour = m//60
        self.min = m%60

    def __repr__(self):
        return f"{self.hour:02d}:{self.min:02d}"

    def __eq__(self, other):
        return self.hour==other.hour and self.min==other.min

    def __add__(self, minutes):
        m = ((60*self.hour + self.min + minutes)%mins_in_days + mins_in_days)%mins_in_days
        self.hour = m//60
        self.min = m%60
        return f"{self.hour:02d}:{self.min:02d}"

    def __sub__(self, minutes):
        m = ((60*self.hour + self.min - minutes)%mins_in_days + mins_in_days)%mins_in_days
        self.hour = m//60
        self.min = m%60
        return f"{self.hour:02d}:{self.min:02d}"
