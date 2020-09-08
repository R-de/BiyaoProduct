from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import time

def get_products():
    """
    提取商品信息
    """
    doc = pq(browser.page_source)
    items = doc('.supplier-recommen').children().items()
    for item in items:
        product = {
            'supplier':item.find('.supplier').text(),
            'title':item.find('.title').text(),
            'price':item.find('.price').attr('price'),
            'evaluate':item.find('.evaluate').text()
        }
        print(product,)
    return

if __name__ == '__main__':
	browser = webdriver.Chrome()
	wait = WebDriverWait(browser, 10)
	url = "http://www.biyao.com/classify/search.html?query=bag"
	browser.get(url)
	for i in range(0, 10):
		browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
		time.sleep(3)
	get_products()