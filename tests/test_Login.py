from datetime import datetime
import pytest

from Pages.AccountPage import AccountPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application("kumbhare_pranay.cs@ghrce.raisoni.net","Pranay_12345")
        assert account_page.display_status_of_edit_your_account_information()

    def test_login_with_invalid_email_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(),"Pranay_12345")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_with_valid_email_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("kumbhare_pranay.cs@ghrce.raisoni.net","198y1")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("","")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def generate_email_with_time_stamp(self):
        # date time
        time_stamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        return "pranay" + time_stamp + "@gmail.com"


