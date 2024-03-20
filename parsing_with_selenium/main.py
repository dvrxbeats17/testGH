from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://ru.wikipedia.org")
print(driver.title)

search_input = driver.find_element(by=By.ID, value="searchInput")
print(search_input)

search_button = driver.find_element(by=By.CSS_SELECTOR, value="form > div > .searchButton")


# divs = driver.find_elements(by=By.TAG_NAME, value="div")
# print(divs)

actions = (ActionChains(driver).send_keys_to_element(search_input, 'питон').click(on_element=search_button))
actions.perform()

chapter_headers = driver.find_elements(By.CLASS_NAME, "toclevel-1>a>.toctext")
for header in chapter_headers:
    print(header.text)

print()