from selenium.webdriver.common.by import By


class OrderPageLocators():

    ORDER_HEADER = By.XPATH, "//div[@class='Order_Header__BZXOb' and text()='Для кого самокат']"
    INPUT_NAME = By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[contains(@placeholder, 'Имя')]"
    INPUT_SURNAME = By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[contains(@placeholder, 'Фамилия')]"
    INPUT_ADDRESS =  By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[contains(@placeholder, 'Адрес')]"
    SELECT_SUBWAY = By.XPATH, "//input[contains(@placeholder, 'Станция метро')]"
    SELECT_LIST_SUBWAY = By.CLASS_NAME, "select-search__options"

    @staticmethod
    def select_station_subway(station):
        return By.XPATH, f"//li[@class='select-search__row']//button[.//div[contains(@class, 'Order_Text__2broi') and text()='{station}']]"

    @staticmethod
    def complete_station(station):
        return By.XPATH, f"//input[@value='{station}']"

    INPUT_TELEPHONE = By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[contains(@placeholder, 'Телефон')]"
    ORDER_NEXT_BUTTON = By.XPATH, "//div[@class = 'Order_NextButton__1_rCA']/button[text()='Далее']"
    ORDER_HEADER_ABOUT_RENT = By.XPATH, "//div[@class='Order_Header__BZXOb' and text()='Про аренду']"
    INPUT_DATA_PIKER = By.CLASS_NAME, "react-datepicker__input-container"
    ORDER_DATA_PIKER = By.CLASS_NAME, "react-datepicker"

    @staticmethod
    def select_data_on_piker(date_piker):
        return By.XPATH, f"//div[contains(@class, 'react-datepicker')]//div[contains(@class, 'react-datepicker__day') and text()='{date_piker}']"

    @staticmethod
    def select_data_in_input(date_piker):
        return By.XPATH, f"//div[@class='react-datepicker__input-container']//input[contains(@value, '{date_piker}')]"

    INPUT_DROPDOWN_RENTAL_PERIOD = By.CLASS_NAME, "Dropdown-control"
    MENU_DROPDOWN_RENTAL_PERIOD = By.CLASS_NAME, "Dropdown-menu"

    @staticmethod
    def select_dropdown_rental_period( rental_period):
        return By.XPATH, f"//div[@class='Dropdown-option' and text()='{rental_period}']"

    @staticmethod
    def input_select_rental_period(rental_period):
        return By.XPATH, f"//div[contains(@class, 'is-selected') and text()='{rental_period}']"

    @staticmethod
    def checkbox_color(color):
        return By.XPATH, f"//label[text()='{color}']"

    SELECT_CHECKBOX_COLOR = By.XPATH, "//div[contains(@class, 'FilledContainer')]"
    INPUT_COMMENT = By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[contains(@placeholder, 'Комментарий для курьера')]"
    ORDER_FINAL_BUTTON = By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/button[text()='Заказать']"
    ORDER_MODAL_HEADER = By.XPATH, "//div[@class = 'Order_ModalHeader__3FDaJ'and text()='Хотите оформить заказ?']"
    ORDER_MODAL_SURE_BUTTON = By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/button[text()='Да']"
    ORDER_MODAL_HEADER_SUCCESSFULLY_PLACED = By.XPATH, "//div[@class = 'Order_ModalHeader__3FDaJ'and text()='Заказ оформлен']"

    # Подтверждение заказа
    button_yes_confirm_order = (By.XPATH, "//button[text()='Да']")
    button_check_status_of_order = (By.XPATH, ".//*[text()='Посмотреть статус']")