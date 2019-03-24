from behave import *
import time


@given("I login into the application")
def step_login(context):
    context.driver.find_element_by_name("userName").send_keys("mercury")
    context.driver.find_element_by_name("password").send_keys("mercury")
    context.driver.find_element_by_name("login").click()
    time.sleep(1)


@then('I search for flight with default value')
def step_default_flight_search(context):
    context.driver.find_element_by_name("findFlights").click()


@then('I reserve for flight with default value')
def step_default_reserve_flight(context):
    context.driver.find_element_by_name("reserveFlights").click()


@then('I enter passenger details')
def step_default_reserve_flight(context):
    context.driver.find_element_by_name("reserveFlights").click()
