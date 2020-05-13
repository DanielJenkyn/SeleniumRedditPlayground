import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages import *


class TestCases(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(
            "resources/chromedriver",
            options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("http://www.reddit.com/")

    def test_open_reddit(self):
        page = HomePage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_open_subreddit(self):
        page = HomePage(self.driver)

        search_result = page.search_item("gaming")
        self.assertIn("r/gaming", search_result)

        subreddit_page = page.click_subreddit()
        self.assertIn("r/gaming/", subreddit_page.get_url())

    def test_print_top_post(self):
        page = SubredditPage(self.driver)
        page.open("r/gaming")
        self.assertIn("r/gaming/", page.get_url())
        page.print_first_post()

    def test_login(self):
        page = HomePage(self.driver)
        login_page = page.click_login_btn()
        login_page.login()
        self.assertTrue(page.check_login())

    def test_upvote(self):
        page = HomePage(self.driver)
        login_page = page.click_login_btn()
        page = login_page.login()
        page.open("r/gaming")
        page.upvote_if_not_upvoted()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner().run(suite)
