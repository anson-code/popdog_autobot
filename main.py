import pyautogui
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://popdog.click/m?uuid=9ed6649f-0130-4982-b3b3-3ad690399d8f')
browser.get('https://popdog.click')
browser.find_element_by_id('settingsClose').click()
cookie = browser.find_element_by_id('cookie')
while 1:
    try:
        cookie.click()
    except:
        pyautogui.tripleClick()