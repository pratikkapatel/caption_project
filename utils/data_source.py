from utils import read_utils

# test_invalid_login_data = [("einfochips", "Invalid credentials"),("einfochips123", "Invalid credentials")
# ]
#
# test_invalid_login_data1 = [
#      ["einfochips", "Invalid credentials"],
#      ["einfochips123", "Invalid credentials"],
# ]
#
# test_add_valid_hr_data = [
# #      ["het", "het123", "het@gmail.com", "software", "einfo", "0000000000"],
# #      ["heta", "heta123", "heta@gmail.com", "software1", "einfo1", "3400000000"]
# # ]

test_invalid_login_data = read_utils.get_csv_as_list("../test_data/valid_login_data.csv")

test_add_valid_hr_data = read_utils.get_sheet_as_list("../test_data/HR_test_data.xlsx",
                                                            "test_add_valid_hr")