from selenium import webdriver
import sys
import time
sys.path.append('../secret')
import constants

driver = webdriver.Chrome(
    executable_path=r'/Users/jwajunhyeob/Documents/chromedrivercontainer/chromedriver')

txbus_link = 'https://txbus.t-money.co.kr/main.do'
driver.get(txbus_link)

driver.find_element_by_css_selector("#depr_Trml_Nm").click()
time.sleep(3)
driver.find_element_by_css_selector(
    "#areaList01 > li:nth-child(120) > a").click()
driver.find_element_by_css_selector("#arvl_Trml_Nm").click()
time.sleep(3)
driver.find_element_by_css_selector(
    "#areaList02 > li:nth-child(127) > a").click()
driver.find_element_by_css_selector("#onewayInfo > div > p > a").click()
driver.find_element_by_css_selector(
    "#onewayInfo > div > div > div > a:nth-child(1)").click()

# contents > div.cont_wrap > div > div.right_cont > div > div.accordian_table.pc_ver > table > tbody > tr:nth-child(7) > td:nth-child(7) > div > a
# contents > div.cont_wrap > div > div.right_cont > div > div.accordian_table.pc_ver > table > tbody > tr:nth-child(9) > td:nth-child(7) > div > a
# If the class name of the a element is btn_reservation, you have to choice next one.


num = 7

while True:
    left_seats_of_total_seats = driver.find_element_by_css_selector(
        "#contents > div.cont_wrap > div > div.right_cont > div > div.accordian_table.pc_ver > table > tbody > tr:nth-child({}) > td:nth-child(7) > div > a".format(num))
    classname = left_seats_of_total_seats.get_attribute("class")
    if classname == "btn_reseration":
        num = num + 2
        continue
    break
left_seats_of_total_seats.click()


driver.switch_to_alert().accept()


i = 1
line = 1
while True:
    selector = driver.find_element_by_css_selector(
        "#contents > div.cont_wrap > div > div.right_cont > div > div.buy_area > ul > li.menu2 > div > ul.line{} > li:nth-child({})".format(line, i))

    if i == 4:
        i = 1
        line = line + 1
    else:
        i = i + 1

    classname = selector.get_attribute("class")
    if classname == "disabled":
        continue
    if classname == "case1 disabled":
        continue

    break


selector.click()

driver.find_element_by_css_selector(
    "#contents > div.cont_wrap > div > div.right_cont > div > div.buy_area > ul > li.menu4.mgt_type11 > p > a").click()
driver.find_element_by_css_selector(
    "#contents > div.cont_wrap > div > div.right_cont > div > div.private > label:nth-child(2) > input").click()
driver.find_element_by_css_selector(
    "#cardInfo > div:nth-child(34) > table > tbody > tr:nth-child(2) > td > div > div").click()
driver.find_element_by_css_selector(
    "#cardInfo > div:nth-child(34) > table > tbody > tr:nth-child(2) > td > div > div > ul > li:nth-child(4)").click()

driver.find_element_by_css_selector(
    "#cardInfo > div:nth-child(34) > table > tbody > tr:nth-child(3) > td > div > input:nth-child(1)").send_keys(constants.CARD_NUM1)
driver.find_element_by_css_selector(
    "#cardInfo > div:nth-child(34) > table > tbody > tr:nth-child(3) > td > div > input:nth-child(3)").send_keys(constants.CARD_NUM2)
driver.find_element_by_css_selector(
    "#cardInfo > div:nth-child(34) > table > tbody > tr:nth-child(3) > td > div > input:nth-child(5)").send_keys(constants.CARD_NUM3)
driver.find_element_by_css_selector(
    "#cardInfo > div:nth-child(34) > table > tbody > tr:nth-child(3) > td > div > input.input2.input_w6.cardInputs.WV\:카드번호\:true\:minLength\=2\&number").send_keys(constants.CARD_NUM4)
driver.find_element_by_css_selector("#month").send_keys(constants.MONTH)
driver.find_element_by_css_selector("#year").send_keys(constants.YEAR)
driver.find_element_by_css_selector(
    "#cardInfo > div:nth-child(34) > table > tbody > tr:nth-child(5) > td > div > input").send_keys(constants.PASS)
driver.find_element_by_css_selector("#brdt").send_keys(constants.PASSNUM)
driver.find_element_by_css_selector(
    "#cardInfo > div:nth-child(37) > table > tbody > tr:nth-child(1) > td > div > input").send_keys(constants.PASSNUM)
driver.find_element_by_css_selector(
    "#cardInfo > div:nth-child(37) > table > tbody > tr:nth-child(2) > td > div > input:nth-child(3)").send_keys(constants.PHONE1)

driver.find_element_by_css_selector(
    "#cardInfo > div:nth-child(37) > table > tbody > tr:nth-child(2) > td > div > input:nth-child(5)").send_keys(constants.PHONE2)

driver.find_element_by_css_selector("#mobile_pwd").send_keys(constants.PHONE2)
