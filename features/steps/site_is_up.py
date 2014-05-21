from behave import *

@given('I browse to www.powery.net')
def step_impl(context):
  context.browser.visit('http://www.powery.net')
  pass

@when('I look at the page for Archive')
def step_impl(context):
  context.browser.driver.save_screenshot('test.png')
  assert context.browser.is_text_present('Archive')

@then('I should see Archive')
def step_impl(context):
  assert context.failed is False
