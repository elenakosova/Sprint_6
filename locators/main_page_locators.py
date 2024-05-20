from selenium.webdriver.common.by import By


class MainPageLocators:

    MAIN_PAGE = By.CLASS_NAME, "Home_HomePage__ZXKIX"
    ORDER_BUTTON = By.CLASS_NAME, "Button_Button__ra12g"
    ORDER_MIDDLE_BUTTON = By.XPATH, "//div[@class = 'Home_FinishButton__1_cWm']/button[text()='Заказать']"
    DROPDOWN_SECTION = By.CLASS_NAME, "accordion"
    OPEN_DROPDOWN_SECTION = By.XPATH, '//div[not(@hidden)]'

    @staticmethod
    def dropdown_element_question(id):
        return By.ID, f"accordion__heading-{id}"

    @staticmethod
    def dropdown_element_answer(id):
        return By.ID, f"accordion__panel-{id}"

    LOGO_SCOOTER = By.CLASS_NAME, "Header_LogoScooter__3lsAR"
    LOGO_YANDEX = By.CLASS_NAME, "Header_LogoYandex__3TSOI"