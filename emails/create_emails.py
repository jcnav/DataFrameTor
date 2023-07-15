import pandas as pd


def read_file_as_list(name_file, user_limits=0):
    my_list = []
    n = 0
    with open(name_file) as file_name:
        my_lines = file_name.readlines()
        for linea in my_lines:
            my_list.append(linea.strip())
            n += 1
            if user_limits != 0 and n >= user_limits:
                return my_list
    return my_list


if __name__ == '__main__':
    users_list = read_file_as_list("emails.txt")
    data = {'Email': users_list}
    df = pd.DataFrame(data, columns=['Email'])
    df.to_csv('emails_atom.csv', index=False)
