import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_guest_can_add_product_to_basket(browser,url):
    browser.implicitly_wait(15)
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.should_be_add_in_basket()
    page.should_be_same_price()