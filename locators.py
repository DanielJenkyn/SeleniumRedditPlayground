from selenium.webdriver.common.by import By


class HomePageLocators(object):
    SEARCH = (By.ID, 'header-search-bar')
    LOGIN = (By.XPATH, '//a[text()="log in"]')
    GAMING = (By.XPATH, '//a[text()="r/gaming"]')
    # Maybe better to have a more dynamic approach like below rather than
    # hardcoded value
    # GAMING = (By.XPATH, '//a[text()='+query+']')
    LOGIN_IFRAME = (
        By.XPATH, "//iframe[contains(@src,'https://www.reddit.com/login/')]")


class SubredditPageLocators(object):
    SEARCH = (By.ID, 'header-search-bar')
    LOGIN = (By.XPATH, '//a[text()="log in"]')
    PINNED_POST = (By.ID, 't3_dk2wow')
    POST = (By.TAG_NAME, "h3")
    UPVOTE = (By.CSS_SELECTOR, "[aria-label=upvote]")
    DOWNVOTE = (By.CSS_SELECTOR, "[aria-label=downvote]")


class LoginPageLocators(object):
    USERNAME = (By.XPATH, "//input[@id='loginUsername']")
    PASSWORD = (By.XPATH, "//input[@id='loginPassword']")
    SIGN_IN = (By.XPATH, "//button[@type='submit']")
