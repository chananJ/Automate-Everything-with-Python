from selenium import webdriver

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
    driver.get("https://www.ynet.co.il/home/0,7340,L-8,00.html")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by="xpath",value="/html/body/div[12]/div/div/div[1]/div[4]/div[4]/div/div/div/div/div/div[1]/a/h1")
    return element.text

print(main())

