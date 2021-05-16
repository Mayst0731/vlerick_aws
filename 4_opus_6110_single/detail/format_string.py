
def format_date(date_str):
    formatted_date = ''
    try:
        date = get_date(date_str)
        month = month_map(date_str)
        year = get_year(date_str)
        formatted_date = f'{year}-{month}-{date}'
    except:
        pass
    return formatted_date


def get_date(date_str):
    date_list = date_str.split()
    date = date_list[1]
    if len(date)<2:
        date = '0' + date
    return date


def get_year(date_str):
    date_list = date_str.split()
    year = date_list[2]
    return year


def month_map(date_str):
    month = date_str.split()[0]
    month_dict = {'Jan' : '01',
                  'Feb' : '02',
                  'Mar' : '03',
                  'Apr' : '04',
                  'May' : '05',
                  'Jun' : '06',
                  'Jul' : '07',
                  'Aug' : '08',
                  'Sep' : '09',
                  'Oct' : '10',
                  'Nov' : '11',
                  'Dec' : '12'}
    return month_dict.get(month,'')


def course_type(type):
    type_dict = {"": "Onsite",
                 "Day": "Onsite",
                 "Virtual": "Online-Virtual",
                 "Online": "Online-Self-paced"}
    return type_dict.get(type)
