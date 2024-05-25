import allure

from const import Const
from locators.dzen_main_page_locators import DzenMainPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»")
    def open_main_page(self):
        self.open_url(Const.MAIN_PAGE)
        self.wait_element_visibility_of_element_located(MainPageLocators.MAIN_PAGE)

    @allure.step("Проскролить до выпадающего списка «Вопросы о важном»")
    def scroll_to_dropdown_section(self):
        element = self.find_element(MainPageLocators.DROPDOWN_SECTION)
        self.scroll_to_element(element)
        self.wait_element_element_to_be_clickable(MainPageLocators.DROPDOWN_SECTION)

    @allure.step("Найти вопрос")
    def find_dropdown_question(self, id):
        current_question = self.find_element(MainPageLocators.dropdown_element_question(id))
        self.wait_element_visibility_of(current_question)
        return current_question

    @allure.step("Нажать на ответ")
    def tap_on_question(self, id):
        self.click_on_element(MainPageLocators.dropdown_element_question(id))
        self.wait_element_visibility_of_element_located(MainPageLocators.OPEN_DROPDOWN_SECTION)
        current_answer = self.find_element(MainPageLocators.dropdown_element_answer(id))
        self.wait_element_visibility_of_element_located(MainPageLocators.dropdown_element_answer(id))
        return current_answer

    @allure.step("Нажать на логотип «Яндекса»")
    def tap_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)
        self.witch_to_window(1)
        self.wait_element_visibility_of_element_located(DzenMainPageLocators.HEADER_YANDEX_DZEN)

    @allure.step("Нажать на кнопку «Заказать» в хедере страницы")
    def tap_order_header_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Проскролить до инструкции «Как это работает»")
    def scroll_to_middle_button(self):
        element = self.find_element(MainPageLocators.ORDER_MIDDLE_BUTTON)
        self.scroll_to_element(element)
        self.wait_element_element_to_be_clickable(element)

    @allure.step("Нажать на кнопку «Заказать»")
    def tap_order_middle_button(self):
        self.click_on_element(MainPageLocators.ORDER_MIDDLE_BUTTON)