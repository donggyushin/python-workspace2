from selenium import webdriver
from bs4 import BeautifulSoup
import time

phone = "01090411019"
pwd = "nlcfjb1129"
path = "/Users/jwajunhyeob/Documents/chromedrivercontainer/chromedriver"
driver = webdriver.Chrome(path)
driver.get("http://www.facebook.org")
assert "Facebook" in driver.title
elem = driver.find_element_by_name("email")
elem.send_keys(phone)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem = driver.find_element_by_css_selector("#loginbutton input")
elem.submit()
time.sleep(1)
profile = driver.find_elements_by_xpath('//*[@id="u_0_a"]/div[1]/div[1]/div/a')
driver.get(profile[0].get_attribute("href"))
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
information_list = soup.select("#profile_timeline_intro_card")
for info in information_list:
    print(info.text)
