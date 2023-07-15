import pandas as pd
import numpy as np
from numpy.random import randn
from create_list_to_dataset import create_list_phone_number, create_list_from_file
from create_list_to_dataset import create_twitter_account, create_list_password, create_users, create_list_from_file, \
    create_list_from_file_curated, duplicate_list_skipping_str

from trash_functions import *

name_columns = ['Id', 'Phone', 'Email',
                'BTC', 'ETH',
                'Tor_URL', 'Username', 'Password', 'OwnName',
                'Twitter', 'Telegram', 'Whatsapp', 'Skype',
                'Paste', 'Base64', 'MD5', 'SHA1', 'SHA256']

name_files = ["Bitname_URL.csv",
              "Email.csv",
              "BTC_Wallet.csv", "ETH_Wallet.csv",
              "Tor_URL.csv", "Username.csv", "Password.csv", "Keyphrase.csv",
              "MD5.csv", "SHA1.csv", "SHA256.csv",
              "XMR_Wallet.csv", "XRP_Wallet.csv", "ZEC_Wallet.csv", "Zeronet_URL.csv"]

# Other test values "BNB_Wallet.csv", "DASH_Wallet.csv", "DOT_Wallet.csv"

cols = len(name_columns)
rows = 3000
xls_name_out = "dataframe_example.xlsx"
csv_name_out = "dataframe_example.csv"


def create_columns_int_3000():
    return pd.DataFrame(randn(3000, len(name_columns)), columns=name_columns)


def replace_df_column(my_datagram_file, name_column, my_list):
    my_datagram_file = my_datagram_file.drop(labels=name_column, axis=1)
    my_datagram_file[name_column] = my_list
    return my_datagram_file


if __name__ == '__main__':

    # Base dataframe
    my_df = create_columns_int_3000()
    # print_dataframe(my_df)

    # Replace Phone column
    num_phones = create_list_phone_number(3000)
    my_df = replace_df_column(my_df, 'Phone', num_phones)
    # print_dataframe(my_df)

    email_list = create_list_from_file_curated("Email.csv", 3000)
    my_df = replace_df_column(my_df, 'Email', email_list)

    btc_list = create_list_from_file_curated("BTC_Wallet.csv", 3000, 32)
    my_df = replace_df_column(my_df, 'BTC', btc_list)
    eth_list = create_list_from_file_curated("ETH_Wallet.csv", 3000, 8)
    my_df = replace_df_column(my_df, 'ETH', eth_list)

    md5_list = create_list_from_file_curated("MD5.csv", 3000, 32)
    my_df = replace_df_column(my_df, 'MD5', md5_list)
    sha1_list = create_list_from_file_curated("SHA1.csv", 3000, 32)
    my_df = replace_df_column(my_df, 'SHA1', sha1_list)
    sha256_list = create_list_from_file_curated("SHA256.csv", 3000, 32)
    my_df = replace_df_column(my_df, 'SHA256', sha256_list)

    pass_list = create_list_password(3000, 4)
    my_df = replace_df_column(my_df, 'Password', pass_list)
    user_list = create_users(pass_list)
    my_df = replace_df_column(my_df, 'Username', user_list)

    twitter_list = create_twitter_account(3000, 10)
    my_df = replace_df_column(my_df, 'Twitter', twitter_list)

    url_tor_list = create_list_from_file("tor_3000.csv", 3000)
    my_df = replace_df_column(my_df, 'Tor_URL', url_tor_list)

    own_name_list = duplicate_list_skipping_str(url_tor_list, ".")
    my_df = replace_df_column(my_df, 'OwnName', own_name_list)


    # load_series_from_files(name_files)

    # df.to_excel(xls_name_out, index=False)
    with pd.ExcelWriter(xls_name_out) as writer:
        my_df.to_excel(writer, index=False)
    # df.to_csv(csv_name_out, index=False, sep=";")
    # df.to_csv(csv_name_out, index=False, encoding="utf-8")
    my_df.to_csv(csv_name_out, index=False)

