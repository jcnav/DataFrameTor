import requests
import pandas as pd

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
    empty_data = {'address': btc_address, 'total_received': 0,
                  'total_sent': 0,
                  'balance': 0,
                  'unconfirmed_balance': 0,
                  'final_balance': 0,
                  'n_tx': 0,
                  'unconfirmed_n_tx': 0,
                  'final_n_tx': 839
                  }
    try:
        response = requests.get(url, headers=headers, verify=True)  # 'verify=True' verifica el certificado SSL

        if response.status_code == 200:
            data = response.json()  # Parseamos la respuesta JSON
            # Aquí puedes realizar el tratamiento de los datos contenidos en 'data'
            print("Respuesta JSON:")
            print(data)
            return 0, data
        else:
            print(f"Error en la petición. Código de estado: {response.status_code}")
            return 1, empty_data

    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {e}")
        return CODE_SERVER_FORCE_BREAK_CONNECT, empty_data

    # print(e.response.status_code)
    # if e.response.status_code == CODE_SERVER_FORCE_BREAK_CONNECT:
    #     return CODE_SERVER_FORCE_BREAK_CONNECT
    # else:
    #     exit(-1)


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


if __name__ == "__main__":
    # btc_address = "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo"
    # response_json = get_balance_btc(btc_address)
    # get_balance_btc2(btc_address)

    field_list = ['address', 'total_received', 'total_sent', 'balance', 'unconfirmed_balance', 'final_balance', 'n_tx',
                  'unconfirmed_n_tx', 'final_n_tx']

    field_dict = {'address': [], 'total_received': [], 'total_sent': [],
                  'balance': [], 'unconfirmed_balance': [], 'final_balance': [],
                  'n_tx': [], 'unconfirmed_n_tx': [], 'final_n_tx': [], 'code': [] }

    lista_de_listas_vacias = [[] for _ in field_list]

    # Ejemplo: Declarar una lista de 3 listas vacías
    lista_de_listas_vacias = [[] for _ in field_list]

    print(lista_de_listas_vacias)

    exit(0)

    address = []
    total_received = []
    total_sent = []
    balance = []
    unconfirmed_balance = []
    final_balance = []
    n_tx = []
    unconfirmed_n_tx = []
    final_n_tx = []
    code = []

    value_list_btc = get_file_values_in_parentheses("BTC_Wallet.csv")
    data_frame = pd.DataFrame({'BTC': value_list_btc})

    for btc_address in value_list_btc:
        ret_code, response_json = get_balance_btc(btc_address)
        code.append(ret_code)
        address.append(response_json["address"])
        total_received.append(response_json["total_received"])
        total_sent.append(response_json["total_sent"])
        balance.append(response_json["balance"])
        unconfirmed_balance.append(response_json["unconfirmed_balance"])
        final_balance.append(response_json["final_balance"])
        n_tx.append(response_json["n_tx"])
        unconfirmed_n_tx.append(response_json["unconfirmed_n_tx"])
        final_n_tx.append(response_json["final_n_tx"])

        # print(btc_address)

    data_frame["code"] = code
    data_frame["address"] = address
    data_frame["total_received"] = total_received
    data_frame["total_sent"] = total_sent
    data_frame["balance"] = balance
    data_frame["unconfirmed_balance"] = unconfirmed_balance
    data_frame["final_balance"] = final_balance
    data_frame["n_tx"] = n_tx
    data_frame["unconfirmed_n_tx"] = unconfirmed_n_tx
    data_frame["final_n_tx"] = final_n_tx

    write_file_dataframe_out(data_frame, "tomate_out")

    # value_list_json =
    # print(value_list)
