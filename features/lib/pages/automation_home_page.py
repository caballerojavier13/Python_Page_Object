from selenium.webdriver.common.by import By
from base_page_object import BasePage
import time

class AutomationHomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://www.automationpractice.com')

    locator_dictionary = {
        "sign_in": (By.CSS_SELECTOR, '.login'),
        "contact_us": (By.LINK_TEXT, 'Contact us'),
        "sign_out": (By.LINK_TEXT, 'Sign out')
    }

    def sign_in(self):
        self.find_element(*self.locator_dictionary['sign_in']).click()


    class HeaderPage(BasePage):
        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser,
                base_url='http://www.automationpractice.com')
        locator_dictionary = {
            "menu_women": (By.XPATH, "//*[@title='Women']"),
            "menu_dresses": (By.XPATH, "//*[@title='Dresses']"),
            "menu_tshirts": (By.XPATH, "//*[@title='T-shirts']")
        }

        class DressesPage(BasePage):
            def __init__(self, context):
                BasePage.__init__(
                    self,
                    context.browser,
                    base_url='http://www.automationpractice.com')
            locator_dictionary = {
                "summer_dresses": (By.XPATH, "//*[@title='Summer Dresses']")
            }
