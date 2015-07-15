from features.steps.search_page import SearchPage
from behave import given, when, then


@given('I am on search page')
def step_impl(context):
    context.search = SearchPage()
    context.search.open()


@when('Search for {text} text')
def step_impl(context, text):
    context.search.search_for(text)


@then('Search result should contain {link} link on {num} position')
def step_impl(context, link, num):
    assert context.search.expect(link, num)


@then('Search result should not contain {link} link on {num} position')
def step_impl(context, link, num):
    assert not context.search.expect(link, num)