import pandas as pd
import numpy as np
from numpy.random import randn

# from strgen import StringGenerator
import strgen
import random


name_columns = ['Id', 'Phone', 'Email',
                'BTC', 'ETH',
                'Tor_URL', 'Username', 'Password', 'OwnName',
                'Twitter', 'Telegram', 'Whatsapp', 'Skype',
                'Paste', 'Base64', 'MD5', 'SHA1', 'SHA256']

cols = len(name_columns)
rows = 3000
xls_name_out = "dataframe_example.xlsx"
csv_name_out = "dataframe_example.csv"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def create_columns_example():
    df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
    print(df)


def create_columns_int_4():
    df = pd.DataFrame(randn(3000, len(name_columns)), index='A B C D E'.split(), columns=name_columns)
    print(df)


def create_columns_int_3000():
    # df = pd.DataFrame(randn(3000, len(name_columns)), index='A B C D E'.split(), columns=name_columns)
    df = pd.DataFrame(randn(3000, len(name_columns)), columns=name_columns)
    print(df)
    print(df.head)
    print(df.tail)
    return df


def create_phone_number(num_expected_values):
    phone_patterns = ["00[\d]{3}9[\d]{2}[\d]{6}", "+[\d]{3}9[\d]{2}[\d]{6}", "+[\d]{3}-[\d]{9}", "+[\d]{3}[\d]{9}"]
    phone_number_list = []
    for n in range(num_expected_values):
        random_phone_number = strgen.StringGenerator(random.choice(phone_patterns)).render()
        phone_number_list.append(random_phone_number)
    return phone_number_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # df = pd.DataFrame()
    # df = pd.DataFrame(np.random.randint(0, 1000, (rows, cols)), name_columns)
    # df.tail()

    # print_hi('PyCharm')

    # StringGenerator("[\l\d]{10}").render_list(3, unique=True)
    # StringGenerator("(%s\n(?:.{,64}\n){,128}%s)\n").render_list(3, unique=True)
    random_str = strgen.StringGenerator("[\w\d]{10}").render()
    print(random_str)
    # Output 4VX1yInC9S

    # pattern = "^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$"
    # pattern = "^(\(?\+[\d]{3}\)?)\s?([\d]{5})\s?([\d][\s\.-]?){7}$"
    pattern1 = "00[\d]{3}9[\d]{2}[\d]{6}"
    pattern2 = "+[\d]{3}9[\d]{2}[\d]{6}"
    pattern3 = "+[\d]{3}-[\d]{9}"
    #random_str2 = strgen.StringGenerator("[\d]{3}&[\w]{3}&[\p]{2}").render()
    random_str2 = strgen.StringGenerator(pattern3).render()
    print(random_str2)
    print(create_phone_number(15))
