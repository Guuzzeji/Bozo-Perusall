from selenium import webdriver


class Browser():
    def __init__(self, driver: webdriver, headless: bool) -> None:
        # Setting up options
        option = webdriver.FirefoxOptions()
        if headless:
            option.add_argument("--headless")
        option.add_argument("window-size=1280,800")

        # Creating custom user agent
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override",
                               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.9 Safari/537.36")
        option.profile = profile

        # Create browser
        self.driver = driver
        self.driver = webdriver.Firefox(options=option)
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def close_browser(self) -> None:
        self.driver.close()
