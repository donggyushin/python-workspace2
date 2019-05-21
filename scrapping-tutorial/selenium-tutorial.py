from selenium import webdriver


path = "/Users/jwajunhyeob/Documents/chromedrivercontainer/chromedriver"
driver = webdriver.Chrome(path)
driver.get("http://google.com/")
search_box = driver.find_element_by_name("q")
search_box.send_keys("youtube")
search_box.submit()
