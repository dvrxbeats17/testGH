from selenium import webdriver 
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

kaspi_shop_url = "https://kaspi.kz/shop/c/wireless%20chargers/" 

driver = webdriver.Chrome() 
driver.get(kaspi_shop_url) 

close_button = driver.find_element(By.CLASS_NAME, "dialog__close")
close_button.click()


sp = BeautifulSoup(driver.page_source, "html.parser")
datas = sp.find_all(class_ = "item-card__info")
for i in datas:
    name = i.select_one(".item-card__name>a").text,
    price = i.select_one(".item-card__debet>.item-card__prices-price").text,
    feedback = i.select_one(".item-card__rating>a").text
    print(name, price, feedback)

print()