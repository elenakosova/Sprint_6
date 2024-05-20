import allure

from const import Const


class TestNavigationPath:

    @allure.title('Проверка редиректа на лендинг Яндекс.Самокат ')
    @allure.description('Проверяем, что при нажатии на логотип «Самокат» пользователь переходит на лендинг «Самокат»')
    def test_check_open_main_page_tap_logo_scooter(self, order_page):
        order_page.open_order_page()
        order_page.tap_logo_scooter()
        assert Const.MAIN_PAGE == order_page.get_current_url()

    @allure.title('Проверка редиректа на «Яндекс.Дзен» ')
    @allure.description('Проверяем, что при нажатии на логотип «Яндекс» пользователь переходит на Яндекс.Дзен')
    def test_check_open_dzen_page_tap_logo_yandex(self, main_page):
        main_page.open_main_page()
        main_page.tap_logo_yandex()
        assert 'dzen.ru' in main_page.get_current_url()