import os
import sys
import time
import keys
from selenium import webdriver
from selenium.webdriver.common.by import By

profile = keys.profile_url
driver = webdriver.Safari()
url = "https://github.com/login"
repo = sys.argv[1]
user = keys.username
passw = keys.password

#   Login in to github
driver.get(url)
driver.find_element(by=By.ID, value="login_field").send_keys(user)
driver.find_element(by=By.ID, value="password").send_keys(passw)
driver.find_element(by=By.NAME, value="commit").click()
time.sleep(2)
#   Creating a new repo
driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/div[6]/details").click()
driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/div[6]/details/details-menu/a[1]").click()
time.sleep(1)
driver.find_element(by=By.ID, value="repository_name").send_keys(repo)
driver.find_element(by=By.ID, value="repository_auto_init").click()
time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="new_repository"]/div[4]/button').click()
#   Cloning the repo
clone = profile + repo + ".git"
os.system("git clone " + clone)
time.sleep(1)
