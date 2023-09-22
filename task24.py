from datetime import datetime
from datetime import timedelta
import calendar


def find_sundays(year: int):
    sunday = datetime.fromisocalendar(year, 1, 7)
    while sunday.year == year:
        print(sunday.strftime('%a %d %B %Y'))
        sunday += timedelta(weeks=1)


def add_years(current_date, years):
    return current_date + timedelta(
        days=years * (366 if current_date.month == 2 and calendar.isleap(current_date.year) else 365)
    )


if __name__ == '__main__':
    # 1
    print('Task 1\n=====================================')
    date = datetime.now()
    iso_date = date.isocalendar()
    print(f'Номер недели: {iso_date.week}')
    # 2
    print('Task 2\n=====================================')
    print(datetime.fromisocalendar(iso_date.year, iso_date.week, 1).strftime('%a %d %B %H:%M:%S %Y'))
    # 3
    print('Task 3\n=====================================')
    find_sundays(2023)
    # 4
    print('Task 4\n=====================================')

    print(add_years(date, -1))
    print(add_years(date, 0))
    print(add_years(date, 2))
    print(add_years(date, 1))
    print(add_years(datetime(2000, 2, 29), 1))
