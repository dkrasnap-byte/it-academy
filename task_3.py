from datetime import date


def get_date_diff_in_days(date1: date, date2: date):
    return abs(date2 - date1).days


if __name__ == '__main__':
    print(get_date_diff_in_days(date(2026, 10, 13), date(2026, 10, 14)))
    print(get_date_diff_in_days(date(2026, 10, 14), date(2026, 10, 13)))

    print(get_date_diff_in_days(date(2025, 10, 13), date(2026, 10, 14)))
    print(get_date_diff_in_days(date(2026, 10, 14), date(2025, 10, 13)))
