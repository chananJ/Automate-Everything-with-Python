import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    # make browsing easier:
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://github.com/login")
    return driver

def main():
    driver = get_driver()
    driver.find_element(by="id",value="login_field").send_keys("chananjacobs2020@gmail.com")
    time.sleep(2)
    driver.find_element(by="id", value="password").send_keys("Efrat2020!" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/div[1]/div[1]/header/div/div[1]/deferred-side-panel/include-fragment/button").click()
    time.sleep(2)
    element = driver.find_element(by="xpath",value="/html/body/div[1]/div[1]/header/div/div[1]/deferred-side-panel/include-fragment/dialog-helper/dialog/scrollable-region/div/div[1]/nav/nav-list/ul/li[11]/internal-nav-list-group/ul/li[4]/a/span[2]")
    return element.text


    print(driver.current_url)
print(main())
