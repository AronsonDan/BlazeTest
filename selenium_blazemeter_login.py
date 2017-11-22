from selenium import webdriver

chromedriver = "/home/home/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get('https://a.blazemeter.com/app/sign-in')

# get the login form and populate it with the desired values
# form = driver.find_element_by_class_name('form signin-form')
username = driver.find_element_by_class_name("email")
password = driver.find_element_by_class_name("password")

username.send_keys("assignment@blazemeter.com")
password.send_keys("NeverUse*API")

# submit the form
form = driver.find_element_by_class_name('signin-form')
form.submit()

# run an assertion test
try:
    assert 'Workspace Dashboard' in driver.title
    title = driver.find_element_by_class_name('active-workspace').text
    assert title == 'Assignment workspace'
    print('Assertion test passed')
except Exception as e:
    print('Assertion test failed')

driver.close()