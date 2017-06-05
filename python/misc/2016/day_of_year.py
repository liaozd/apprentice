#!/usr/bin/env python


def day_of_year(year, month, day):
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if _is_leap_year(year):
        month_day[1] = 29
    days = sum(month_day[:month - 1]) + day
    print('the date {year}-{month}-{day} is the {days} day of the year {year}.'.format(
        year=year, month=month, day=day, days=_turn_days_to_str(days)
    ))


def _is_leap_year(year):
    """
    :param year: int
    :return: if the year number is leap year
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def _turn_days_to_str(days):
    """
    :param days: int
    :return: turn int day to 1st, 2nd, 3rd or 4th
    """
    if days % 10 == 1:
        return '%dst' % days
    if days % 10 == 2:
        return '%dnd' % days
    if days % 10 == 3:
        return '%drd' % days
    if (days % 10 >= 4) or (days % 10 == 0):
        return '%dth' % days


if __name__ == '__main__':
    day_of_year(2017, 3, 1)
    day_of_year(2016, 3, 1)
