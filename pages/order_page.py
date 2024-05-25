import allure
from const import Const
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage



class OrderPage(BasePage):

    @allure.step("Открыть страницу регистрации (https://qa-scooter.praktikum-services.ru/order' «Яндекс.Самоката»")
    def open_order_page(self):
        self.open_url(Const.ORDER_PAGE)
        self.wait_element_visibility_of_element_located(OrderPageLocators.ORDER_HEADER)

    @allure.step('Нажать на логотип «Самокат» в форме заказа')
    def tap_logo_scooter(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Заполнить поле «Имя»")
    def set_name(self, name):
        self.send_keys(OrderPageLocators.INPUT_NAME, name)

    @allure.step("Заполнить поле «Фамилия»")
    def set_surname(self,surname):
        self.send_keys(OrderPageLocators.INPUT_SURNAME, surname)

    @allure.step("Заполнить поле «Адрес»")
    def set_address(self,address):
        self.send_keys(OrderPageLocators.INPUT_ADDRESS, address)

    @allure.step("Выбрать станцию метро")
    def set_station(self, station):
        self.click_on_element(OrderPageLocators.SELECT_SUBWAY)
        self.wait_element_presence_of_element_located(OrderPageLocators.select_station_subway(station))
        self.click_on_element(OrderPageLocators.select_station_subway(station))
        self.wait_element_visibility_of_element_located(OrderPageLocators.complete_station(station))

    @allure.step("Заполнить поле «Телефон»")
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.INPUT_TELEPHONE, phone)

    def order_about_person_page(self, name, surname, address, station, phone):
        self.open_order_page()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station(station)
        self.set_phone(phone)

    @allure.step("Нажать на кнопку «Далее» на первой странице")
    def tap_next_page_button(self):
        self.click_on_element(OrderPageLocators.ORDER_NEXT_BUTTON)
        self.wait_element_visibility_of_element_located(OrderPageLocators.ORDER_HEADER_ABOUT_RENT)

    @allure.step("Заполнить поле «Когда привезти самокат»")
    def set_data_piker(self, date_piker):
        self.click_on_element(OrderPageLocators.INPUT_DATA_PIKER)
        self.wait_element_presence_of_element_located(OrderPageLocators.ORDER_DATA_PIKER)
        self.click_on_element(OrderPageLocators.select_data_on_piker(date_piker))
        self.wait_element_presence_of_element_located(OrderPageLocators.select_data_in_input(date_piker))

    @allure.step("Заполнить поле «Срок аренды»")
    def set_rental_period(self, rental_period):
        self.click_on_element(OrderPageLocators.INPUT_DROPDOWN_RENTAL_PERIOD)
        self.wait_element_presence_of_element_located(OrderPageLocators.MENU_DROPDOWN_RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.select_dropdown_rental_period(rental_period))
        self.wait_element_presence_of_element_located(OrderPageLocators.input_select_rental_period(rental_period))

    @allure.step("Заполнить поле «Цвет самоката»")
    def set_color(self, color):
        self.click_on_element(OrderPageLocators.checkbox_color(color))
        self.wait_element_visibility_of_element_located(OrderPageLocators.SELECT_CHECKBOX_COLOR)

    @allure.step("Заполнить поле «Комментарии для курьера»")
    def set_comment_delivery(self, comment):
        self.send_keys(OrderPageLocators.INPUT_COMMENT, comment)

    @allure.step("Заполняем все поля на второй странице заказа")
    def order_about_rental_page(self, date_piker, rental_period, color, comment):
        self.set_data_piker(date_piker)
        self.set_rental_period(rental_period)
        self.set_color(color)
        self.set_comment_delivery(comment)

    @allure.step("Нажать на кнопку «Заказать»")
    def tap_order_final_button(self):
        self.click_on_element(OrderPageLocators.ORDER_FINAL_BUTTON)
        self.wait_element_visibility_of_element_located(OrderPageLocators.ORDER_MODAL_HEADER)
        self.click_on_element(OrderPageLocators.ORDER_MODAL_SURE_BUTTON)
        assert self.find_element(OrderPageLocators.ORDER_MODAL_HEADER_SUCCESSFULLY_PLACED)

    @allure.step('Проверить отображение кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.find_element(OrderPageLocators.button_check_status_of_order)