from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(5)


def after_all(context):
    context.browser.quit()