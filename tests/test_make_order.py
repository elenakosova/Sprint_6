import allure
from const import Const
import pytest

from locators.order_page_locators import OrderPageLocators


class TestChekoutPath:

    @allure.title('Кнопка «Заказать» в хедере на лендинге Яндекс Самоката')
    @allure.description('Проверить, что при нажатии на кнопку «Заказать» в хедере сайта, открывается форма заказа')
    def test_check_open_order_page_tap_button_in_header(self, main_page):
        main_page.open_main_page()
        main_page.tap_order_header_button()
        assert Const.ORDER_PAGE == main_page.get_current_url()

    @allure.title('Кнопка «Заказать» внизу страницы на лендинге Яндекс Самоката')
    @allure.description('Проверяем, что при нажатии на кнопку «Заказать» на странице сайта, открывается форма заказа')
    def test_check_open_order_page_tap_midlle_button(self, main_page):
        main_page.open_main_page()
        main_page.scroll_to_middle_button()
        main_page.tap_order_middle_button()
        assert Const.ORDER_PAGE == main_page.get_current_url()

    person_data = [
            ['Райан', 'Гослинг', 'Садовническая 5', 'Сокольники', '79048459222', '28', 'сутки', 'чёрный жемчуг', ''],
            ['Елена', 'Косова', 'Пермь', 'Черкизовская', '79028084295', '26', 'четверо суток', 'серая безысходность', 'На домофоне нажать 0, консерьж отероет'],
        ]
    @allure.title('Проверка флоу заказа самоката на сайте «Яндекс.Самоката»')
    @allure.description('Проверяем, форму заполнения при заказе самоката')
    @pytest.mark.parametrize("name, surname, address, station, phone, date_piker, rental_period, color, comment", person_data)
    def test_check_pop_up_window_successful_order(self, order_page, name, surname, address, station, phone, date_piker, rental_period, color, comment):
        order_page.order_about_person_page(name, surname, address, station, phone)
        order_page.tap_next_page_button()
        order_page.order_about_rental_page(date_piker, rental_period, color, comment)
        order_page.tap_order_final_button()
        assert order_page.find_element(OrderPageLocators.ORDER_MODAL_HEADER_SUCCESSFULLY_PLACED)