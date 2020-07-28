from selenium import webdriver
from datetime import date, datetime
from time_sheet_properties import *

def login_gw():
    driver.find_element_by_id('UserName').send_keys(ID)
    driver.find_element_by_id('Password').send_keys(PW)
    driver.find_element_by_xpath('//*[@alt="로그인"]').click()

def move_time_sheet():
    driver.find_element_by_xpath('//*[contains(text(), "타임시트")]').click()
    driver.find_element_by_xpath('//*[@nm="타임시트등록"]').click()

def get_today():
    now = datetime.now()
    text_date = date(now.year, now.month, now.day)
    return text_date

def apply_time_sheet():
    today_button = driver.find_element_by_xpath('//*[contains(text(), "' + get_today().isoformat() + '")]')
    if today_button.get_attribute('style') == '':
        today_button.click()
        driver.find_element_by_xpath('//*[contains(text(), "{}")]'.format(PROJECT_ID)).click()
        driver.find_element_by_xpath('//*[@id="btnAdd"]').click()
        driver.find_element_by_xpath('//*[@id="chkSels"]').click()
        driver.find_element_by_xpath('//*[@id="btnSave"]').click()
        alert = driver.switch_to.alert
        alert.accept()
    driver.quit()

# 1. chrome driver load
driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.implicitly_wait(5)
# 2. login page 이동
driver.get('http://gw.emro.co.kr/Account/LogOn')
driver.implicitly_wait(5)
# 3. 로그인
login_gw()
driver.implicitly_wait(5)
# 4. 타임시트 이동
move_time_sheet()
driver.implicitly_wait(5)
# 5. 타임시트 등록
apply_time_sheet()

