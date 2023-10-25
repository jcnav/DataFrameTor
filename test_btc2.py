import requests
import pandas as pd
import time

import urllib.request
from bs4 import BeautifulSoup
from create_list_to_dataset import get_file_values_in_parentheses

CODE_SERVER_FORCE_BREAK_CONNECT = 10054


def get_balance_btc(btc_address):
    """

    :param btc_address:
    :return:
        {
         'address': '34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo',
         'total_received': 109389822149494,
         'total_sent': 84530083091124,
         'balance': 24859739058370,
         'unconfirmed_balance': 0,
         'final_balance': 24859739058370,
         'n_tx': 839,
         'unconfirmed_n_tx': 0,
         'final_n_tx': 839
         }
    """
    url = f'https://api.blockcypher.com/v1/btc/main/addrs/{btc_address}/balance'
    print(url)
    headers = {'User-Agent': 'PostmanRuntime/7.32.3'}
    empty_data = {'address': btc_address, 'total_received': 0, 'total_sent': 0,
                  'balance': 0, 'unconfirmed_balance': 0, 'final_balance': 0,
                  'n_tx': 0, 'unconfirmed_n_tx': 0, 'final_n_tx': 839
                  }
    try:
        response = requests.get(url, headers=headers, verify=True)  # 'verify=True' verifica el certificado SSL

        if response.status_code == 200:
            data = response.json()  # Parseamos la respuesta JSON
            print(f"Respuesta JSON: {data}")
            return 0, data
        else:
            print(f"Error en la petición. Código de estado: {response.status_code}")
            return 1, empty_data

    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {e}")
        return CODE_SERVER_FORCE_BREAK_CONNECT, empty_data


def get_balance_btc2(btc_address):
    url = f'https://api.blockcypher.com/v1/btc/main/addrs/{btc_address}/balance'
    print(url)

    datos = urllib.request.urlopen(url)
    soup = BeautifulSoup(datos.read(), "html.parser")

    print(soup)


def write_file_dataframe_out(my_df, name_out):
    with pd.ExcelWriter(name_out + ".xlsx") as writer:
        my_df.to_excel(writer, index=False)
    # df.to_csv(csv_name_out, index=False, sep=";")
    # df.to_csv(csv_name_out, index=False, encoding="utf-8")
    my_df.to_csv(name_out + ".csv", index=False)


def build_dataframe_btc(df_complete, btc_list):
    df_complete["code"] = btc_list["code"]
    df_complete["address"] = btc_list["address"]
    df_complete["total_received"] = btc_list["total_received"]
    df_complete["total_sent"] = btc_list["total_sent"]
    df_complete["balance"] = btc_list["balance"]
    df_complete["unconfirmed_balance"] = btc_list["unconfirmed_balance"]
    df_complete["final_balance"] = btc_list["final_balance"]
    df_complete["n_tx"] = btc_list["n_tx"]
    df_complete["unconfirmed_n_tx"] = btc_list["unconfirmed_n_tx"]
    df_complete["final_n_tx"] = btc_list["final_n_tx"]
    return data_frame


if __name__ == "__main__":
    # btc_address = "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo"
    # response_json = get_balance_btc(btc_address)
    # get_balance_btc2(btc_address)

    field_dict = {'address': [], 'total_received': [], 'total_sent': [],
                  'balance': [], 'unconfirmed_balance': [], 'final_balance': [],
                  'n_tx': [], 'unconfirmed_n_tx': [], 'final_n_tx': [], 'code': [] }

    value_list_btc = get_file_values_in_parentheses("BTC_Wallet.csv")
    data_frame = pd.DataFrame({'BTC': value_list_btc})

    for btc_address in value_list_btc:
        sleeping_time = 5
        for i in range(10):
            ret_code, response_json = get_balance_btc(btc_address)
            if ret_code == CODE_SERVER_FORCE_BREAK_CONNECT:
                time.sleep(sleeping_time)
                sleeping_time += 10
                print(f"Waiting {sleeping_time} for {btc_address}. Fail")
            else:
                print(f"Consulted {btc_address}. OK")
                break
        field_dict["code"].append(ret_code)
        field_dict["address"].append(response_json["address"])
        field_dict["total_received"].append(response_json["total_received"])
        field_dict["total_sent"].append(response_json["total_sent"])
        field_dict["balance"].append(response_json["balance"])
        field_dict["unconfirmed_balance"].append(response_json["unconfirmed_balance"])
        field_dict["final_balance"].append(response_json["final_balance"])
        field_dict["n_tx"].append(response_json["n_tx"])
        field_dict["unconfirmed_n_tx"].append(response_json["unconfirmed_n_tx"])
        field_dict["final_n_tx"].append(response_json["final_n_tx"])

    data_frame = build_dataframe_btc(data_frame, field_dict)
    write_file_dataframe_out(data_frame, "out_btc")

    # value_list_json =
    # print(value_list)
