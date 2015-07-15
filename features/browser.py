from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import re


class Browser(object):

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    def visit(context, url, location=''):
        context.driver.get(url + location)

    def close(context):
        context.driver.quit()

    def find(context, selector):
        return context.driver.find_element_by_css_selector(selector)

    def find_by_name(context, name):
        return context.driver.find_element_by_name(name)

    def fill_in(context, field, text):
        field.clear()
        field.send_keys(text)
        field.submit()

    def wait_for_title(context, text):
        WebDriverWait(context.driver, 5).until(
            EC.title_contains(text)
        )

    # def wait_for_load(context, text):
    #     lru = context.driver.current_url[::-1]
    #     txet = text[::-1].replace(' ', '\+')
    #     WebDriverWait(context.driver, 5).until(
    #         lambda matcher: re.match(txet, lru)
    #     )

    def wait_for_element(context, selector):
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
        )