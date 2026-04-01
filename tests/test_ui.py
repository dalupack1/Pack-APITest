from selenium import webdriver
from selenium.webdriver.common.by import By

def test_ui_loads():
    driver = webdriver.Chrome()
    driver.get("https://dogapi.dog")

    assert "Dog API" in driver.title
    driver.quit()

def test_ui_has_content():
    driver = webdriver.Chrome()
    driver.get("https://dogapi.dog")

    body = driver.find_element(By.TAG_NAME, "body").text
    assert "Dog" in body

    driver.quit()