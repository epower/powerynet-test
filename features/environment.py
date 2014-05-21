from splinter import Browser

def before_scenario(context, scenario):
  context.browser = Browser('phantomjs')

def after_scenario(context, scenario):
  context.browser.quit()


