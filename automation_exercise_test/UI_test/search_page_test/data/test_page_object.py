import time

from playwright.sync_api import Page

class ProductPageObject:
    def __init__(self, page: Page):
        self.page = page

    def cookie_btn(self):
        locator = self.page.locator('xpath=/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]/p')
        locator.wait_for()
        return locator

    def women_link(self):
        locator = self.page.get_by_role("link", name=" Women")
        locator.wait_for()
        return locator

    def dress_list_item_women(self):
        locator = self.page.get_by_role("listitem").filter(has_text="Dress")
        locator.wait_for()
        return locator

    def tops_list_item_women(self):
        locator = self.page.get_by_role("listitem").filter(has_text="Tops")
        locator.wait_for()
        return locator

    def saree_list_item_women(self):
        locator = self.page.get_by_role("listitem").filter(has_text="Saree")
        locator.wait_for()
        return locator

    def link_men(self):
        locator = self.page.get_by_role("link", name=" Men")
        locator.wait_for()
        return locator

    def tshirts_list_men(self):
        locator = self.page.get_by_role("listitem").filter(has_text="Tshirts")
        locator.wait_for()
        return locator


    def jeans_list_men(self):
        locator = self.page.get_by_role("listitem").filter(has_text="Jeans")
        locator.wait_for()
        return locator


    def link_kids(self):
        locator = self.page.get_by_role("link", name=" Kids")
        locator.wait_for()
        return locator


    def dress_list_kids(self):
        locator = self.page.get_by_role("listitem").filter(has_text="Dress")
        locator.wait_for()
        return locator


    def tops_shirts_list_kids(self):
        locator = self.page.get_by_role("listitem").filter(has_text="Tops & Shirts")
        locator.wait_for()
        return locator


    def polo_link(self):
        locator = self.page.get_by_role("link", name="(6) Polo")
        locator.wait_for()
        return locator


    def hm_link(self):
        locator = self.page.get_by_role("link", name="(5) H&M")
        locator.wait_for()
        return locator


    def madame_link(self):
        locator = self.page.get_by_role("link", name="(5) Madame")
        locator.wait_for()
        return locator


    def mast_harbour_link(self):
        locator = self.page.get_by_role("link", name="(3) Mast & Harbour")
        locator.wait_for()
        return locator


    def babyhug_link(self):
        locator = self.page.get_by_role("link", name="(4) Babyhug")
        locator.wait_for()
        return locator


    def allen_solly_junior_link(self):
        locator = self.page.get_by_role("link", name="(3) Allen Solly Junior")
        locator.wait_for()
        return locator


    def kookie_kids_link(self):
        locator = self.page.get_by_role("link", name="(3) Kookie Kids")
        locator.wait_for()
        return locator


    def biba_link(self):
        locator = self.page.get_by_role("link", name="(5) Biba")
        locator.wait_for()
        return locator


    def add_to_cart(self, index: int):
        # locator = self.page.locator(f'.overlay-content [data-product-id="{index}"]')
        # locator_hov = self.page.locator(f'.productinfo.text-center [data-product-id="{index}"]')
        locator = self.page.locator(f"(//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart'])[{index * 2}]")
        # locator = self.page.locator(f".btn.btn-default.add-to-cart").nth((index - 1) * 2)
        card = self.page.locator('.product-image-wrapper').nth(index - 1)
        card.hover()
        locator.wait_for()
        return locator

    def count_add_to_cart(self):
        locator = self.page.locator(f'[data-product-id]')
        return locator.count()


    def continue_shopping(self):
        locator = self.page.get_by_role("button", name="Continue Shopping")
        locator.wait_for()
        return locator


    def view_cart(self):
        locator = self.page.get_by_role("link", name="View Cart")
        locator.wait_for()
        return locator


    def view_product(self, index):
        locator = self.page.locator(".nav.nav-pills.nav-justified").nth(index - 1)
        locator.wait_for()
        return locator

    def view_product_count(self):
        locator = self.page.locator(".nav.nav-pills.nav-justified")
        return locator.count()


    def search_product_place_holder(self, to_fill):
        locator = self.page.locator("#search_product")
        locator.wait_for()
        locator.fill(to_fill)


    def submit_search_btn(self):
        locator = self.page.locator("#submit_search")
        locator.wait_for()
        return locator

    def scroll_up(self):
        self.page.mouse.wheel(0, 1000)
        locator = self.page.locator("#scrollUp")
        locator.wait_for()
        return locator

    def cart_btn(self):
        locator = self.page.locator('a[href="/view_cart"]').nth(0)
        locator.wait_for()
        return locator

