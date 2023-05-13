from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tkinter

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://app.senecalearning.com/courses")
driver.implicitly_wait(5)

old_element = None

while True:
    selected_element = driver.find_elements(By.XPATH, "//*[contains(@class, 'Input_focused__')]")

    if len(selected_element) != 0 and selected_element[0] != old_element:
        old_element = selected_element[0]
        text_element = selected_element[0].find_element(By.XPATH, "../preceding-sibling::span/span")
        selected_element[0].send_keys(text_element.get_attribute("innerHTML"))


