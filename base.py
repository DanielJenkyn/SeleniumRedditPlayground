class Page(object):
    def __init__(self, driver, base_url="http://www.reddit.com/"):
        self.base_url = base_url
        self.driver = driver
        # Pretty high timeout, different bandwidth/latency etc
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)
