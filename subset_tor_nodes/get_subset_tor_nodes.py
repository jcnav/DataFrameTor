import pandas as pd


def read_file_as_list(name_file, tor_limits, header=False):
    my_list = []
    n = 0
    if header:
        tor_limits += 1

    with open(name_file) as file_name:
        my_lines = file_name.readlines()
        for linea in my_lines:
            pair_users = linea.split(",")
            my_list.append(pair_users[2])
            n += 1
            if n >= tor_limits:
                break
                # return my_list
    my_list.remove("Destination")

    return my_list


if __name__ == '__main__':
    tor_list = read_file_as_list("tor_nodes.csv", 3000, header=True)
    data = {'Tor_URL': tor_list}
    df = pd.DataFrame(data, columns=['Tor_URL'])
    df.to_csv('tor_3000.csv', index=False)
