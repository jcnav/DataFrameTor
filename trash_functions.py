from numpy.random import randn
import pandas as pd


def create_columns_example():
    df2 = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
    print(df2)


def create_columns_int_4():
    name_columns = ['Id', 'Phone', 'Email',
                    'BTC', 'ETH',
                    'Tor_URL', 'Username', 'Password', 'OwnName',
                    'Twitter', 'Telegram', 'Whatsapp', 'Skype',
                    'Paste', 'Base64', 'MD5', 'SHA1', 'SHA256']
    df2 = pd.DataFrame(randn(3000, len(name_columns)), index='A B C D E'.split(), columns=name_columns)
    print(df2)


def print_dataframe(my_df):
    print(my_df)
    print(my_df.head)
    print(my_df.tail)

