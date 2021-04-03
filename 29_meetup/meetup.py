import calendar
from datetime import date


class MeetupDayException(Exception):
    pass


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    cal: calendar.Calendar = calendar.Calendar()
    # all those days in month
    matching_days: list[date] = [d for w in cal.monthdatescalendar(year, month) for d in w
                                 if d.month == month and d.weekday() == list(calendar.day_name).index(day_of_week)]
    if week.endswith("teenth"):
        return [d for d in matching_days if 13 <= d.day <= 19][0]
    elif week == "last":
        return matching_days[-1]
    elif week[0].isdigit() and int(week[0]) <= len(matching_days):
        return matching_days[int(week[0]) - 1]
    else:
        raise MeetupDayException("No match found")


print(meetup(2013, 5, "teenth", "Monday"))