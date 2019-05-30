import time

from behave import *

use_step_matcher("re")


@given("Monique is on the welcome page")
def step_impl(context):
    context.browser.get('https://road-dev.herokuapp.com/welcome/')
    assert context.browser.title == "Road Improvement System - Welcome"


@when("She selects the book recommendation button")
def step_impl(context):
    book_button = context.browser.find_element_by_id('recommendation')
    book_button.click()


@then("Monique see the book Extreme Programming Installed")
def step_impl(context):
    authors = context.browser.find_element_by_id('authors')
    assert 'Chet Hendrickson' in authors
