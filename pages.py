import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Users
from base import Page
from locators import *


class HomePage(Page):
    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        # Check if can find search bar, if yes then presume page has loaded
        return True if self.find_element(*self.locator.SEARCH) else False

    # This is one method that could be improved, currently GAMING is a
    # hardcoded value, should use query
    def search_item(self, query: str = "gaming"):
        self.find_element(*self.locator.SEARCH).send_keys(query)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        item = WebDriverWait(self, self.timeout).until(
            EC.presence_of_element_located(
                (self.locator.GAMING[0], self.locator.GAMING[1])))
        return item.text

    def click_subreddit(self):
        self.find_element(*self.locator.GAMING).click()
        return SubredditPage(self.driver)

    def click_login_btn(self):
        self.find_element(*self.locator.LOGIN).click()
        return self.switch_to_login_page()

    def switch_to_login_page(self) -> Page:
        WebDriverWait(self.driver, self.timeout).until(
            EC.frame_to_be_available_and_switch_to_it(
                self.find_element(*self.locator.LOGIN_IFRAME)))
        return LoginPage(self.driver)

    def check_login(self):
        # return true if login button has gone
        return WebDriverWait(self, self.timeout).until(
            EC.invisibility_of_element_located(
                (self.locator.LOGIN[0], self.locator.LOGIN[1])))


class SubredditPage(Page):
    def __init__(self, driver):
        self.locator = SubredditPageLocators
        super().__init__(driver)

    def print_first_post(self):
        print(self.get_post(0))

    # 0 indexed
    def get_post(self, index: int):
        posts = self.find_elements(*self.locator.POST)
        if len(posts) > 0:
            print(posts[index].text)

    # 0 indexed
    def get_upvote(self, index: int = 1):
        upvotes = WebDriverWait(self, self.timeout).until(
            EC.presence_of_all_elements_located(
                (self.locator.UPVOTE[0], self.locator.UPVOTE[1])))
        if len(upvotes) > 0:
            return upvotes[index]

    def get_downvote(self, index: int = 1):
        downvotes = WebDriverWait(self, self.timeout).until(
            EC.presence_of_all_elements_located(
                (self.locator.DOWNVOTE[0], self.locator.DOWNVOTE[1])))
        if len(downvotes) > 0:
            return downvotes[index]

    def upvote_if_not_upvoted(self):
        upvote = self.get_upvote(1)
        downvote = self.get_downvote(1)
        if upvote.get_attribute("aria-pressed") == "false":
            # Here is where something goes wrong - Element cannot be clicked
            upvote.click()
        else:
            downvote.click()


class LoginPage(Page):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    def enter_email(self, user: str = "user1"):
        username_field = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(
                (self.locator.USERNAME[0], self.locator.USERNAME[1])))

        username_field.click()
        username_field.send_keys(Users.get_user(user)[0])

    def enter_password(self, user: str = "user1"):
        password_field = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(
                (self.locator.PASSWORD[0], self.locator.PASSWORD[1])))
        password_field.click()
        password_field.send_keys(Users.get_user(user)[1])

    def click_signin(self):
        self.find_element(*self.locator.SIGN_IN).click()

    def login(self):
        self.enter_email()
        self.enter_password()
        self.click_signin()
        self.driver.switch_to.default_content()
        return SubredditPage(self.driver)
