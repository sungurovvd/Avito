from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def add_from_card(url):
    driver.get(url)

    add_to_favorites_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button/span'))
    )
    add_to_favorites_button.click()

    driver.get("https://www.avito.ru/favorites")

    favorites_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div[1]/div/div/div[1]/a/img'))
    )
    print("Product added in Fav from the Card")

def remove_item(xpath):
    url = 'https://www.avito.ru/favorites'
    driver.get(url)
    item_to_remove = driver.find_element(By.XPATH, xpath)
    remove_button = item_to_remove.find_element(By.XPATH, './div[1]/div')
    remove_button.click()
    print("Product deleted from Fav")


def add_from_search(item_url, xpath):
    driver.get(item_url)

    add_to_favorites_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    add_to_favorites_button.click()

    driver.get("https://www.avito.ru/favorites")
    print("Product added to Fav from Search")

try:
    url = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
    add_from_card(url)

    remove_item('//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div/div/div/div[2]')

    item_url = "https://www.avito.ru/all/avtomobili/audi-ASgBAgICAUTgtg3elyg?q=%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C"
    add_from_search(item_url, '//*[@id="i3178923347"]/div/div/div[2]/div[1]/div')
except Exception as e:
    print('Error:', e)
finally:
    driver.quit()