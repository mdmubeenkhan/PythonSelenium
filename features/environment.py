from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("http://newtours.demoaut.com/")


def after_all(context):
    context.driver.quit()

