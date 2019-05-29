import time

from behave import given, when, then, use_step_matcher, step

use_step_matcher("re")

pause = 0


@given("I am on the login page")
def step_impl(context):
    # context.browser.get('http://localhost:' + str(context.port) + '/login')
    context.browser.get('https://road-dev.herokuapp.com/login/')
    # print('http://localhost:' + str(context.port) + '/login')
    assert context.browser.title == "Road Improvement System - Login"

    time.sleep(pause)


@when("I enter a valid username and password")
def step_impl(context):
    username = context.browser.find_element_by_id('username')
    username.send_keys("user")
    time.sleep(pause)
    password = context.browser.find_element_by_id('password')
    password.send_keys("pass")
    time.sleep(pause)
    context.browser.find_element_by_id('submit').click()
    time.sleep(pause)


@then("I should see the welcome page")
def step_impl(context):
    # assert context.browser.title == "Road Improvement System - Welcome"
    pass

@when("I enter an invalid username or password")
def step_impl(context):
    username = context.browser.find_element_by_id('username')
    username.send_keys("wrong user")
    time.sleep(pause)
    password = context.browser.find_element_by_id('password')
    password.send_keys("wrong password")
    time.sleep(pause)
    context.browser.find_element_by_id('submit').click()
    time.sleep(pause)


@then("I expect to be on the login page")
def step_impl(context):
    assert context.browser.title == "Road Improvement System - Login"


@step("I expect to see an error message")
def step_impl(context):
    message = context.browser.find_element_by_id('message').text
    assert message == "Incorrect Username/Password. Please try again."


@when("I am missing a username")
def step_impl(context):
    username = context.browser.find_element_by_id('username')
    username.send_keys("")
    time.sleep(pause)
    password = context.browser.find_element_by_id('password')
    password.send_keys("wrong password")
    time.sleep(pause)
    context.browser.find_element_by_id('submit').click()
    time.sleep(pause)


@step("I expect to see an missing field error")
def step_impl(context):
    message = context.browser.find_element_by_id('message').text
    assert message == "Missing Username"


@given("I am on the welcome page")
def step_impl(context):
    context.browser.get('https://road-dev.herokuapp.com/welcome/')
    assert context.browser.title == "Road Improvement System - Welcome"


@then("I expect to see the correct welcome message")
def step_impl(context):
    welcome_message = context.browser.find_element_by_id('welcome').text
    assert welcome_message == "Welcome to the Road Improvement System!\nThe best site for information on pot holes."
