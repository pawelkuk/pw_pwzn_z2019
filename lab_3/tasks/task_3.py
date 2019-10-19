from itertools import groupby
import pytz
"""
Zadanie za 2 pkt.

Uzupełnij funckję parse_dates tak by zwracała przygotowaną wiadomość
z posortowanymi zdarzeniami.
Funkcja przyjmuje ciag zdarzeń (zapisanych w formie timestampu w dowolnej strefie czasowej),
przetwarza je na zdarzenia w strefie czasowej UTC i sortuje.
Posortowane zdarzenia są grupowane na dni i wypisywane od najnowszych do najstarszych.

Na 1pkt. Uzupełnij funkcję sort_dates, która przyjmuje dwa parametry:
- log (wielolinijkowy ciąg znaków z datami) zdarzeń
- format daty (podany w assercie format ma być domyślnym)
Zwraca listę posortowanych obiektów typu datetime w strefie czasowej UTC.

Funkcje group_dates oraz format_day mają pomoc w grupowaniu kodu.
UWAGA: Proszę ograniczyć użycie pętli do minimum.
"""
import datetime
import calendar

def sort_dates(date_str, date_format=''):
    """
    Parses and sorts given message to list of datetimes objects descending.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: sorted desc list of utc datetime objects
    :rtype: list
    """
    tmp = date_str.strip().split('\n')
    unsorted_strptime_list = list(map(lambda x: x.strip().split(' '), tmp))
    month_to_number_dict = { k:str(v) for v, k in enumerate(calendar.month_abbr)}
    for row in unsorted_strptime_list:
        row[2] = month_to_number_dict[row[2]]
    unsorted_strptimes = list(map(lambda x: ' '.join(x[1:]), unsorted_strptime_list))
    unsorted_datetimes = list(map(
        lambda x: datetime.datetime.strptime(x, '%d %m %Y %H:%M:%S %z'),
        unsorted_strptimes))
    return sorted(unsorted_datetimes, reverse=True)


def group_dates(dates):
    """
    Groups list of given days day by day.

    :param dates: List of dates to group.
    :type dates: list
    :return:
    """
    return groupby(dates, lambda x: x.date())

def format_day(day, events):
    """-0700
    Formats message for one day.

    :param day: Day object.
    :type day: datettime.datetime
    :param events: List of events of given day
    :type events: list
    :return: parsed message for day
    :rtype: str
    """
    pass


def parse_dates(date_str, date_format=''):
    """
    Parses and groups (in UTC) given list of events.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: parsed events
    :rtype: str
    """
    dates = sort_dates(date_str)
    grouped_by_day = group_dates(dates)
    result = []
    for day, dates in grouped_by_day:
        result.append(str(day))
        for date in dates:
            result.append('\t' + str(date.astimezone(pytz.utc).time()))
        result.append('----')
    result.pop()
    return '\n'.join(result)

if __name__ == '__main__':
    dates = """
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000
    """
    assert sort_dates(dates) == [
        datetime.datetime(2015, 5, 10, 20, 54, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 10, 13, 54, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 2, 14, 24, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 1, 13, 54, 36, tzinfo=datetime.timezone.utc),
    ]

    assert parse_dates(dates) == """2015-05-10
\t20:54:36
\t13:54:36
----
2015-05-02
\t14:24:36
----
2015-05-01
\t13:54:36"""