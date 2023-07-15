import pandas as pd


def read_file_as_list(name_file, user_limits):
    my_list = []
    n = 0
    with open(name_file) as file_name:
        my_lines = file_name.readlines()
        for linea in my_lines:
            pair_users = linea.split(",")
            my_list.append(pair_users[0])
            n += 1
            if n >= user_limits:
                return my_list
    return my_list


if __name__ == '__main__':
    users_list = read_file_as_list("users.csv", 3000)
    data = {'users': users_list}
    df = pd.DataFrame(data, columns=['users'])
    df.to_csv('users_3000.csv', index=False)


