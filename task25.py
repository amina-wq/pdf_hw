import calendar

from datetime import datetime


def generate_calendar(year, month):
    cal = calendar.monthcalendar(year, month)

    month_name = calendar.month_name[month]
    days_of_week = calendar.day_name

    html = f"<html><head><title>{month_name} {year} Календарь</title></head><body>"
    html += f"<h1>{month_name} {year} Календарь</h1>"

    html += "<table border='1'><tr>"
    for day in days_of_week:
        html += f"<th>{day}</th>"
    html += "</tr>"

    for week in cal:
        html += "<tr>"
        for day in week:
            if day == 0:
                html += "<td></td>"
            else:
                html += f"<td>{day}</td>"
        html += "</tr>"

    html += "</table></body></html>"

    with open(f"calendar_{year}_{month}.html", "w") as f:
        f.write(html)


if __name__ == '__main__':
    # 1
    print('Task 1\n=====================================')
    print(f'Местное время: {datetime.now()}')
    print(f'Время по Гринвичу: {datetime.utcnow()}')
    # 2
    print('Task 2\n=====================================')
    timedelta = datetime(2023, 9, 22, 22, 1, 6) - datetime(2021, 9, 22, 23, 20, 3)
    print(timedelta.days)
    # 3
    print('Task 3\n=====================================')
    print(timedelta)
    # 4
    generate_calendar(2023, 9)
