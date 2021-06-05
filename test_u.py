# Generated by Selenium IDE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent
from helpers import type
from random import randint

accounts = []

class TestU():
  def setup_method(self):
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')
    options.add_argument(r"user-data-dir=C:\Users\Charles\AppData\Local\Google\Chrome\User%23Data\Default")
    options.add_argument("profile-directory=Profile 2")
    self.driver = webdriver.Chrome(options=options)
    self.driver.implicitly_wait(10)
  def teardown_method(self):
    time.sleep(50)
    self.driver.quit()

  
  def test_u(self, email, password, username):
    # Test name: u
    # Step # | name | target | value | comment
    # 1 | open | https://playvalorant.com/en-us/ |  | 
    self.driver.get("https://playvalorant.com/en-us/")
    time.sleep(randint(1,5))
    # 2 | setWindowSize | 1917x981 |  | 
    self.driver.set_window_size(1917, 981)
    # 3 | click | css=.HomeHero-module--downloadButton--3BblN .PrimaryButton-module--label-text--23ce5 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".HomeHero-module--downloadButton--3BblN .PrimaryButton-module--label-text--23ce5").click()
    time.sleep(randint(1,5))
    # 4 | mouseOver | css=.PrimaryButton-module--default--2alKM:nth-child(2) .PrimaryButton-module--label-text--23ce5 |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".PrimaryButton-module--default--2alKM:nth-child(2) .PrimaryButton-module--label-text--23ce5")
    time.sleep(randint(1,5))
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 5 | click | css=.PrimaryButton-module--default--2alKM:nth-child(2) .PrimaryButton-module--label-text--23ce5 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".PrimaryButton-module--default--2alKM:nth-child(2) .PrimaryButton-module--label-text--23ce5").click()
    time.sleep(randint(1,5))
    # 6 | click | name=email |  | 
    self.driver.find_element(By.NAME, "email").click()
    # 7 | type | name=email | charles6huang+owo@gmail.com | 
    type(self.driver.find_element(By.NAME, "email"), email[0]+'+'+username+'@'+email[1])
    time.sleep(randint(1,5))
    # 8 | sendKeys | name=email | ${KEY_ENTER} | 
    self.driver.find_element(By.NAME, "email").send_keys(Keys.ENTER)
    time.sleep(randint(1,5))
    # 9 | type | name=date_of_birth_day | 19 | 
    self.driver.find_element(By.NAME, "date_of_birth_day").send_keys("19")
    time.sleep(randint(1,5))
    time.sleep(2)
    # 10 | type | name=date_of_birth_month | 09 | 
    self.driver.find_element(By.NAME, "date_of_birth_month").send_keys("09")
    time.sleep(randint(1,5))
    time.sleep(2)
    # 11 | type | name=date_of_birth_year | 1999 | 
    self.driver.find_element(By.NAME, "date_of_birth_year").send_keys("1999")
    time.sleep(randint(1,5))
    time.sleep(2)
    # 12 | click | css=.mobile-button |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".mobile-button").click()
    time.sleep(randint(1,5))
    # 13 | type | name=username |
    type(self.driver.find_element(By.NAME, "username"),username)
    # 14 | click | css=.mobile-button |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".mobile-button").click()
    time.sleep(randint(1,5))
    time.sleep(2)
    # 15 | click | name=password |  | 
    self.driver.find_element(By.NAME, "password").click()
    time.sleep(randint(1,5))
    time.sleep(2)
    # 16 | click | name=password |  | 
    self.driver.find_element(By.NAME, "password").click()
    time.sleep(randint(1,5))
    time.sleep(2)
    # 17 | doubleClick | name=password |  | 
    element = self.driver.find_element(By.NAME, "password")
    time.sleep(randint(1,5))
    time.sleep(2)
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 18 | type | name=password | Jaygay123 | 
    type(self.driver.find_element(By.NAME, "password"), password)
    time.sleep(randint(1,5))
    # 19 | click | name=confirm_password |  | 
    self.driver.find_element(By.NAME, "confirm_password").click()
    time.sleep(randint(1,5))
    # 20 | type | name=confirm_password | Jaygay123 | 
    type(self.driver.find_element(By.NAME, "confirm_password"), password)
    time.sleep(randint(1,5))
    # 21 | click | css=.mobile-button |  |
    time.sleep(randint(1,5))
    self.driver.find_element(By.CSS_SELECTOR, ".mobile-button").click()
    # 22 | mouseOver | css=.mobile-button |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".mobile-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    accounts.append(username)
    print("success")


email = "charles6huang@gmail.com".split("@")
password = "Jaygay123"
username = "ButteryBippo"
account_total = 3
create_account = TestU()
for x in range(account_total):

    create_account.setup_method()
    create_account.test_u(email, password, username+str(x))
    create_account.teardown_method()

time.sleep(randint(1,5))
print(accounts)
