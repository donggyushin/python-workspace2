from selenium import webdriver

path = "/Users/jwajunhyeob/Documents/chromedrivercontainer/chromedriver"
driver = webdriver.Chrome(path)
driver.get("http://www.facebook.org")
assert "Facebook" in driver.title
logout_button = driver.find_element_by_css_selector("#u_13_5")
logout_button.submit()
