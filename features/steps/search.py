import re
from behave import given, when, then
import time


@given('I am on search page')
def step_impl(context):
    context.browser.get('http://www.google.com')


@when('Search for {text} text')
def step_impl(context, text):
    search_field = context.browser.find_element_by_name('q')
    search_field.clear()
    search_field.send_keys(text)
    search_field.submit()


@then('Search result should contain {link} link on {num} position')
def step_impl(context, link, num):
    #  res = context.browser.find_elements_by_css_selector('.r>a')
    # script = "return document.querySelectorAll('.r > a')[" + str(int(num)-1) + "].innerHTML"
    time.sleep(3)
    value = context.browser.execute_script("return document.querySelectorAll('.r > a')["+str(int(num)-1)+"].innerHTML")
    print(value)
    assert re.search(link.lower(), value.lower())


@then('Search result should not contain {link} link on {num} position')
def step_impl(context, link, num):
    time.sleep(3)
    value = context.browser.execute_script("return document.querySelectorAll('.r > a')["+str(int(num)-1)+"].innerHTML")
    print(value)
    assert not re.search(link.lower(), value.lower())