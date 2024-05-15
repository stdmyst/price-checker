from selenium import webdriver as wd
from selenium.webdriver.common.by import By

import time
#from bs4 import BeautifulSoup as Soup
#import requests
#import lxml


'''    
def get_price(url):
    req = requests.get(url)
    print(req.status_code)
    soup = Soup(req.text, "lxml")
    text = soup.find("span", class_="Money-module__money_UZBbh").text
    text = text.replace(",", ".")
    flag = 0
    result = ""
    for num in text:
        if flag and not num.isdigit():
            break
        elif num == ".":
            flag = 1
            result += num
        if num.isdigit():
            result += num
    return float(result)
'''


def get_price(url):
    options = wd.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = wd.Chrome(options=options)
    driver.get(url)
    time.sleep(1)
    el = driver.find_element(By.CLASS_NAME, 'Money-module__money_UZBbh').text
    el = el.replace("\n", "").replace(",", ".")
    res = ""
    flag = 1
    for symb in el:
        if symb.isdigit() or symb == ".":
            res += symb
        else:
            break
    return(float(res))
