import strgen
import random
from random import SystemRandom

NO_VALUE = "NaN"


def _create_list_from_patterns(num_expected_values, patterns):
    """
    Create a list with values that matches with one pattern
    :param num_expected_values: number of item in the list
    :param patterns: pattern expected
    :return: For now only works with phone numbers
    """
    phone_number_list = []
    for n in range(num_expected_values):
        random_phone_number = strgen.StringGenerator(random.choice(patterns)).render()
        phone_number_list.append(random_phone_number)
    return phone_number_list


def create_list_phone_number(num_expected_values):
    """
    Create a list with phone number values
    :param num_expected_values: Number of expected items in the list
    :return: The phone number list
    """
    phone_patterns = ["00[\d]{3}9[\d]{2}[\d]{6}", "+[\d]{3}9[\d]{2}[\d]{6}", "+[\d]{3}-[\d]{9}", "+[\d]{3}[\d]{9}",
                      NO_VALUE, NO_VALUE, NO_VALUE, NO_VALUE, NO_VALUE, NO_VALUE, NO_VALUE, NO_VALUE]
    return _create_list_from_patterns(num_expected_values, phone_patterns)


def create_password(size_pass_max=18):
    """
    This function creates one random password
    :param size_pass_max: Maximum lenght of the password
    :return: The password string
    """
    # set_values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    set_values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>@#%&+"
    cryptogen = SystemRandom()

    size_passwd = random.randint(8, size_pass_max)
    p = ""
    while size_passwd > 0:
        p = p + cryptogen.choice(set_values)
        size_passwd = size_passwd - 1
    return p


def create_users(pass_list):
    user_references = _read_file_as_list("data//users_3000.csv")
    users_list = []
    n = 0
    for password in pass_list:
        if password == NO_VALUE:
            users_list.append(NO_VALUE)
        else:
            users_list.append(user_references[n])
        n += 1
    return users_list


def create_twitter_account(num_expected_values, rnd=1):
    """
    Create a list with random twitter account numbers from a file with twitter accounts
    :param num_expected_values:
    :param rnd: Porcentage of the None -NaN- values
    :return: One account twitter list
    """
    user_references = _read_file_as_list("data//users_3000.csv")
    users_list = []
    n = 0
    for n in range(num_expected_values):
        is_random = random.randint(1, rnd)  # Only works 1/rnd
        if is_random == 1:
            my_account = "@"+user_references[n]
            print(my_account)
            users_list.append(my_account)
        else:
            users_list.append(NO_VALUE)
    return users_list


def create_list_password(num_expected_values, rnd=1):
    password_list = []
    for n in range(num_expected_values):
        is_random = random.randint(1, rnd)  # Only works 1/rnd
        if is_random == 1:
            random_pass = create_password()
            password_list.append(random_pass)
        else:
            password_list.append(NO_VALUE)
    return password_list


def _read_file_as_list(name_file):
    """
    Read a file and convert to list. One row is one item in the list
    :param name_file: Name of the file
    :return: List with read values from file
    """
    my_list = []
    with open(name_file) as file_name:
        my_lines = file_name.readlines()
        for linea in my_lines:
            my_list.append(linea.strip('\n'))
    return my_list


def _get_substring_list_from_to(my_list, s_from="(", s_to=")"):
    """
    Clean seed list used as template for my test file. Remove the substring (xxx...xxx) or other from different pattern
    :param my_list: original list
    :param s_from: initial substring
    :param s_to: final substring
    :return: curated list
    """
    dst_list = []
    for my_value in my_list:
        from_str = my_value.split(s_from)
        to_str = from_str[1].split(s_to)
        dst_list.append(to_str[0])
    return dst_list


def _get_str_in_parentheses_list(my_list):
    return _get_substring_list_from_to(my_list, "(", ")")


def get_file_values_in_parentheses(name_file):
    """
    Read a file removing substring between parenthesis -included-
    :param name_file: name file
    :return: curated list from file
    """
    value_list = _read_file_as_list("data//" + name_file)
    return _get_str_in_parentheses_list(value_list)


def create_list_set(size_list, value):
    my_list = []
    for n in range(size_list):
        my_list.append(value)
    return my_list


def set_weight_nan(size_list, typical_value, nan_value):
    weight_list = create_list_set(size_list, typical_value)
    weight_list.append(nan_value)
    return weight_list


def get_random_list(value_list, weight_rnd, num_expected_values):
    my_list = []
    page_size = len(value_list)

    if num_expected_values < page_size:
        print(f"Error: Must be use a minimum expected set of {page_size}")

    num_pages = int(num_expected_values/page_size)
    for n in range(num_pages):
        random_email = random.choices(value_list, weight_rnd, k=len(weight_rnd))
        my_list += random_email

    random_email = random.choices(value_list, weight_rnd, k=num_expected_values-len(my_list))
    my_list += random_email

    return my_list


# def get_random_list(value_list, weight_rnd, num_expected_values):
#     my_list = []
#     for n in range(num_expected_values):
#         random_email = random.choices(value_list, weight_rnd, k=1)
#         my_list += random_email
#     return my_list


def create_list_from_file(name_file, num_expected_values, nan_probability=4):
    """
    Create a list with values from file name_file
    :param name_file:
    :param num_expected_values: Number of expected values
    :param nan_probability: Inclusion probability of nan values
    :return: list with generated values
    """
    value_list = get_file_values_in_parentheses(name_file)

    weight_rnd = set_weight_nan(len(value_list), 1, nan_probability)
    value_list.append(NO_VALUE)

    return get_random_list(value_list, weight_rnd, num_expected_values)


def load_series_from_files(name_files):
    for name_file in name_files:
        print(get_file_values_in_parentheses(name_file))




