from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def wait_element_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def wait_element_presence_of_element_located(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def wait_element_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_element_visibility_of(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(locator))

    def get_text(self, locator):
        return self.find_element(locator).text

    def witch_to_window(self,number):
        self.driver.switch_to.window(self.driver.window_handles[number])

    def get_current_url(self):
        return self.driver.current_url

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)