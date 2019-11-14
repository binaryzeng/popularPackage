from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text(("Sign in"))
signin_link.click()

username_box = browser.find_element_by_id(("login_field"))
username_box.send_keys("my name")
pwd_box = browser.find_element_by_id(("password"))
pwd_box.send_keys("password!!!")
pwd_box.submit()

# assert "hello Jason" in browser.page_source
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "Hello Jason" in link_label
