import datetime
from datetime import timedelta


def date_range(stream):

    for index in range(0, len(stream)-1):
        couple_of_dates = stream[index:index+2]
        range_of_dates = []
        dates = []

        for data in couple_of_dates:
            try:
                d = datetime.datetime.strptime(data, "%Y-%m-%d").date()
                range_of_dates.append(d)
            except ValueError:
                pass

        try:
            start_date = range_of_dates[0]
            end_date = range_of_dates[1]
            delta_date = end_date - start_date
            for i in range(delta_date.days + 1):
                dates.append(start_date + timedelta(i))
        except IndexError:
            pass

        print(dates)


def delete_and_return_last_user1():

    default_list = ['A100', 'A101', 'A102']
    for i in range(0, len(default_list)-1):

        element_to_delete = default_list[-1]
        default_list.remove(element_to_delete)
        print(default_list, default_list[-1])


DEFAULT_USER_COUNT = 3
def delete_and_return_last_user(region, default_list=['A100', 'A101', 'A102']):

    element_to_delete = default_list[-1]
    default_list.remove(element_to_delete)
    return default_list[DEFAULT_USER_COUNT - 2]


if __name__ == '__main__':
    #date_range(['2020-1-12', '2020-2-14', '2020-2-17'])
    #delete_and_return_last_user1()
    delete_and_return_last_user(1)