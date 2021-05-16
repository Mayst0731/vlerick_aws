import re


def get_currency(price):
    if 'eur' in price or 'EUR' in price:
        currency = 'EUR'
    return currency


def get_symbol_currency(txt):
    currency = ''
    if '$' in txt:
        currency = 'USD'
    elif '€' in txt:
        currency = 'EUR'
    else:
        currency = get_currency(txt)
    return currency


def format_date(date_str):
    date_str = date_str.strip()
    date_list = date_str.split('/')
    date = date_list[0]
    month = date_list[1]
    year = date_list[-1]
    formatted_date = f'{year}-{month}-{date}'
    return formatted_date


def month_dict(month_str):
    months_check = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12',
    }
    for key in months_check:
        if key in month_str:
            return months_check[key]


def find_date(str):
    date = re.findall('\d{1,2}', str)[0]
    return date


def find_year(str):
    year = re.findall('\d{4}', str)[0]
    return year


def find_directly_start_date1(str):
    year = find_year(str)
    month = month_dict(str)
    date = find_date(str)
    start_date = f'{year}-{month}-{date}'
    return start_date


def filter_locations(locations):
    clean_locations = []
    useless_locations = ['Vlerick','Campus',',']

    for loc in locations:
        if loc not in useless_locations:
            clean_locations.append(loc)
    return clean_locations
