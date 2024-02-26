from datetime import datetime
import pytest

from Pages.AccountSuccessPage import AccountSuccessPage
from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage


def generate_email_with_time_stamp():
    time_stamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    return "pranay" + time_stamp + "@gmail.com"


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Pranay", "Kumbhare",
                                                                 generate_email_with_time_stamp(), "1234567890",
                                                                 "12345", "12345", "no", "select")
        expected_heading = 'Your Account Has Been Created!'
        account_success_page.retrieved_account_creation_message().__eq__(expected_heading)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Pranay", "Kumbhare",
                                                                 generate_email_with_time_stamp(), "1234567890",
                                                                 "12345", "12345", "yes", "select")
        expected_heading = 'Your Account Has Been Created!'
        account_success_page.retrieved_account_creation_message().__eq__(expected_heading)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Pranay", "Kumbhare", "pranay1@gmail.com", "1234567890", "12345", "12345",
                                          "yes", "select")
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning_message)

    def test_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("", "", "", "", "", "", "no", "no")
        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!",
                                                 "First Name must be between 1 and 32 characters!",
                                                 "Last Name must be between 1 and 32 characters!",
                                                 "E-Mail Address does not appear to be valid!",
                                                 "Telephone must be between 3 and 32 characters!",
                                                 "Password must be between 4 and 20 characters!")
