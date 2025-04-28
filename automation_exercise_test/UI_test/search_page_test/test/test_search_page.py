import logging
import random
import time

import allure
from playwright.sync_api import Page

from automation_exercise_test.UI_test.search_page_test.data.test_page_object import ProductPageObject


# def test_scroll_up(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     time.sleep(5)
#     pw_open.mouse.click(31, 613)
#     time.sleep(3)
#     pobj.scroll_up().click()
#     y_position = pw_open.evaluate('window.scrollY')
#     assert y_position == 0
#
# def test_count_add_to_cart(pw_open):
#     page = pw_open
#     page.goto('https://www.automationexercise.com/products', wait_until='load')
#     page.get_by_role('button', name='Соглашаюсь').click()
#     pobj = ProductPageObject(page)
#     count = pobj.count_add_to_cart()
#     logging.info(f"Полученное значение count: {count}")
#     assert count == 68
#
# def test_women_link(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.women_link().click()
#     pw_open.wait_for_load_state()
#     assert pobj.dress_list_item_women().is_visible()
#     assert pobj.tops_list_item_women().is_visible()
#     assert pobj.saree_list_item_women().is_visible()
#
# def test_men_link(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.link_men().click()
#     pw_open.wait_for_load_state()
#     assert pobj.tshirts_list_men().is_visible()
#     assert pobj.jeans_list_men().is_visible()
#
# def test_kids_link(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.link_kids().click()
#     pw_open.wait_for_load_state()
#     assert pobj.dress_list_kids()
#     assert pobj.tops_shirts_list_kids().is_visible()
#
# def test_polo_link(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.polo_link().click()
#     pw_open.wait_for_load_state()
#     assert pw_open.url.endswith('/brand_products/Polo')
#
# def test_hm_link(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.hm_link().click()
#     pw_open.wait_for_load_state()
#     assert pw_open.url.endswith('/brand_products/H&M')
#
# def test_madame_link(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.madame_link().click()
#     pw_open.wait_for_load_state()
#     assert pw_open.url.endswith('/brand_products/Madame')
#
# def test_mast_harbour_link(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.mast_harbour_link().click()
#     pw_open.wait_for_load_state()
#     assert pw_open.url.endswith('/brand_products/Mast%20&%20Harbour')
#
# def test_babyhug_link(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.babyhug_link().click()
#     pw_open.wait_for_load_state()
#     assert pw_open.url.endswith('/brand_products/Babyhug')
#
# def test_allen_solly_junior_link(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.allen_solly_junior_link().click()
#     pw_open.wait_for_load_state()
#     assert pw_open.url.endswith('/brand_products/Allen%20Solly%20Junior')
#
# def test_kookie_kids_link(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.kookie_kids_link().click()
#     pw_open.wait_for_load_state()
#     assert pw_open.url.endswith('/brand_products/Kookie%20Kids')
#
# def test_biba_link(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.biba_link().click()
#     pw_open.wait_for_load_state()
#     assert pw_open.url.endswith('/brand_products/Biba')
#
# def test_add_to_cart34(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.add_to_cart(34).click()
#     pw_open.wait_for_load_state()
#     assert pobj.continue_shopping().is_visible()
#
# def test_add_to_cart_r(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.add_to_cart(random.randint(2, 33)).click()
#     pw_open.wait_for_load_state()
#     assert pobj.continue_shopping().is_visible()
#
# def test_add_to_cart1(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.add_to_cart(1).click()
#     pw_open.wait_for_load_state()
#     assert pobj.continue_shopping().is_visible()
#
# def test_view_product_count(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn()
#     counted = pobj.view_product_count()
#     assert counted == 34
#
# def test_view_product1(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.view_product(1).click()
#     pw_open.wait_for_load_state()
#     assert pw_open.url.endswith('/product_details/1')
#
# def test_view_product34(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.view_product(34).click()
#     pw_open.wait_for_load_state()
#     assert pw_open.url.endswith('/product_details/43')
#
# def test_view_product9(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.view_product(9).click()
#     pw_open.wait_for_load_state()
#     assert pw_open.url.endswith('/product_details/11')
#
# def test_search_product_place_holder(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.search_product_place_holder('Men Tshirt')
#     pobj.submit_search_btn().click()
#     pw_open.wait_for_load_state('load')
#     assert pw_open.get_by_text('Men Tshirt').nth(0).is_visible()
#
# def test_view_cart(pw_open: Page):
#     pobj = ProductPageObject(pw_open)
#     pobj.cookie_btn().click()
#     pobj.add_to_cart(34).click()
#     pobj.view_cart().click()
#     pw_open.wait_for_load_state()
#     assert pw_open.locator('#product-43')

def test_continue_shopping(pw_open: Page):
    pobj = ProductPageObject(pw_open)
    with allure.step('нажатие кнопки согласится с куки'):
        try:
            pobj.cookie_btn().click(timeout=3000)  # попробуй 3 секунды
        except:
            pass  # Если нет кнопки — ничего страшного
    with allure.step('добавить в корзину товар 1'):
        pobj.add_to_cart(1).click()
    with allure.step('продолжить покупки нажатие'):
        pobj.continue_shopping().click()
    with allure.step('скролл к локатору корзина если нужно'):
        pobj.cart_btn().scroll_into_view_if_needed()
    with allure.step('нажатие кнопки корзина'):
        pobj.cart_btn().click()
    with allure.step('загрузка страницы'):
        pw_open.wait_for_load_state()
    with allure.step('проверка товара в корзине'):
        assert pw_open.locator("#product-1").is_visible()

