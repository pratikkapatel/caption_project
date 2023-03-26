from utils import read_utils

test_add_valid_employee_data = [
    ["tobi.mylan2@gmail.com", "Tobi@2020", "John Wick", "wick@gmail.com", "Engineer"]]


# test_add_valid_employee_data = read_utilites.get_sheet_as_list("../test_data/selenium.xlsx", "test_add_valid_employee")
# test_invalid_profile_upload_data = read_utilites.get_sheet_as_list("../test_data/selenium.xlsx","test_invalid_profile_upload")
test_invalid_login_data = read_utils.get_csv_as_list("../test_data/test_invalidLogin.csv")