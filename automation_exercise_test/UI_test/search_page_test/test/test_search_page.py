import random
import allure


def test_count_add_to_cart(product_page):
    count = product_page.count_add_to_cart()
    with allure.step('проверка количества товаров на странице'):
        assert count == 68

def test_women_link(product_page, page):
    
    with allure.step('нажатие кнопки women'):
        product_page.women_link().click()
    page.wait_for_load_state()
    with allure.step('проверка появления ссылок после нажатия women'):
        assert product_page.dress_list_item_women().is_visible()
        assert product_page.tops_list_item_women().is_visible()
        assert product_page.saree_list_item_women().is_visible()

def test_men_link(product_page, page):
    
    with allure.step('нажатие кнопки men'):
        product_page.link_men().click()
    page.wait_for_load_state()
    with allure.step('проверка появления ссылок после нажатия men'):
        assert product_page.tshirts_list_men().is_visible()
        assert product_page.jeans_list_men().is_visible()

def test_kids_link(product_page, page):
    
    with allure.step('нажатие кнопки kids'):
        product_page.link_kids().click()
    page.wait_for_load_state()
    with allure.step('проверка появления ссылок после нажатия kids'):
        assert product_page.dress_list_kids()
        assert product_page.tops_shirts_list_kids().is_visible()

def test_polo_link(product_page, page):
    
    with allure.step('нажатие кнопки polo'):
        product_page.polo_link().click()
    page.wait_for_load_state()
    with allure.step('проверка адреса страницы после нажатия polo'):
        assert page.url.endswith('/brand_products/Polo')

def test_hm_link(product_page, page):
    
    with allure.step('нажатие кнопки hm_link'):
        product_page.hm_link().click()
    page.wait_for_load_state()
    with allure.step('проверка ссылки после нажатия HM'):
        assert page.url.endswith('/brand_products/H&M')

def test_madame_link(product_page, page):
    
    with allure.step('нажатие кнопки madame'):
        product_page.madame_link().click()
    page.wait_for_load_state()
    with allure.step('проверка страницы мадам'):
        assert page.url.endswith('/brand_products/Madame')

def test_mast_harbour_link(product_page, page):
    
    with allure.step('нажатие кнопки харбор'):
        product_page.mast_harbour_link().click()
    page.wait_for_load_state()
    with allure.step('проверка страницы харбор'):
        assert page.url.endswith('/brand_products/Mast%20&%20Harbour')

def test_babyhug_link(product_page, page):
    
    with allure.step('нажатие кнопки бебихаг'):
        product_page.babyhug_link().click()
    page.wait_for_load_state()
    with allure.step('проверка страницы бебихаг'):
        assert page.url.endswith('/brand_products/Babyhug')

def test_allen_solly_junior_link(product_page, page):
    
    with allure.step('нажатие кнопки аллен солли'):
        product_page.allen_solly_junior_link().click()
    page.wait_for_load_state()
    with allure.step('проверка страницы аллен солли'):
        assert page.url.endswith('/brand_products/Allen%20Solly%20Junior')

def test_kookie_kids_link(product_page, page):
    
    with allure.step('нажатие кнопки kookie'):
        product_page.kookie_kids_link().click()
    page.wait_for_load_state()
    with allure.step('проверка страницы kookie'):
        assert page.url.endswith('/brand_products/Kookie%20Kids')

def test_biba_link(product_page, page):
    
    with allure.step('нажатие кнопки биба'):
        product_page.biba_link().click()
    page.wait_for_load_state()
    with allure.step('проверка страницы биба'):
        assert page.url.endswith('/brand_products/Biba')

def test_add_to_cart34(product_page, page):
    
    with allure.step('добавление товара 34 клик'):
        product_page.add_to_cart(34).click()
    page.wait_for_load_state()
    with allure.step('проверка попаппа с кнопкой продолжить покупки'):
        assert product_page.continue_shopping().is_visible()

def test_add_to_cart_r(product_page, page):
    
    with allure.step('добавить в корзину рандомный товар'):
        product_page.add_to_cart(random.randint(2, 33)).click()
    page.wait_for_load_state()
    with allure.step('проверка видимости кнопки "продолжить покупки"'):
        assert product_page.continue_shopping().is_visible()

def test_add_to_cart1(product_page, page):
    
    with allure.step('добавление товара 1 в корзину клик'):
        product_page.add_to_cart(1).click()
    page.wait_for_load_state()
    with allure.step('проверка наличия кнопки продолжить покупки'):
        assert product_page.continue_shopping().is_visible()

def test_view_product_count(product_page):
    
    counted = product_page.count_view_product_cards()
    with allure.step('проверка количества карточек товара'):
        assert counted == 34

def test_view_product1(product_page, page):
    
    with allure.step('посмотреть товар 1 нажатие'):
        product_page.view_product(1).click()
    page.wait_for_load_state()
    with allure.step('проверка страницы 1 товара'):
        assert page.url.endswith('/product_details/1')

def test_view_product34(product_page, page):
    
    product_page.view_product(34).click()
    page.wait_for_load_state()
    assert page.url.endswith('/product_details/43')

def test_view_product9(product_page, page):
    
    with allure.step('просмотр страницы 9 товара'):
        product_page.view_product(9).click()
    page.wait_for_load_state()
    with allure.step('проверка страницы 9 товара'):
        assert page.url.endswith('/product_details/11')

def test_search_product_place_holder(product_page, page):
    
    with allure.step('заполниние плейсхолдера для поиска товаров Men Tshirt'):
        product_page.search_product_place_holder('Men Tshirt')
    with allure.step('нажатие кнопки поиска'):
        product_page.submit_search_btn().click()
    page.wait_for_load_state('load')
    with allure.step('проверка наличия нужного товара на странице после поиска'):
        assert page.get_by_text('Men Tshirt').nth(0).is_visible()

def test_continue_shopping(product_page, page):
    
    with allure.step('добавить в корзину товар 1'):
        product_page.add_to_cart(1).click()
    with allure.step('продолжить покупки нажатие'):
        product_page.continue_shopping().click()
    with allure.step('скролл к локатору корзина если нужно'):
        product_page.cart_btn().scroll_into_view_if_needed()
    with allure.step('нажатие кнопки корзина'):
        product_page.cart_btn().click()
    with allure.step('загрузка страницы'):
        page.wait_for_load_state()
    with allure.step('проверка товара в корзине'):
        assert page.locator("#product-1").is_visible()

def test_view_cart(product_page, page):
    
    with allure.step('добавить в коризину 34 товар'):
        product_page.add_to_cart(34).click()
    with allure.step('кнопка просмотр корзины'):
        product_page.view_cart().click()
    page.wait_for_load_state()
    with allure.step('проверка наличия товара 34(43) в корзине'):
        assert page.locator('#product-43').is_visible()

def test_scroll_up(product_page, page):
    
    page.wait_for_timeout(5000)
    with allure.step('свернуть рекламу, клик'):
        page.mouse.click(31, 613)
    page.wait_for_timeout(5000)
    with allure.step('кнопка scroll клик'):
        product_page.scroll_up().click()
    page.wait_for_timeout(2000)
    y_position = page.evaluate('window.scrollY')
    with allure.step('проверка положения страницы после клика'):
        assert y_position == 0