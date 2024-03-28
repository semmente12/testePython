from time import sleep
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

screenWidth, screenHeight = pyautogui.size()
options = webdriver.ChromeOptions()
options.add_argument(f"--window-size={screenWidth},{screenHeight}")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://3dlab.nuvemdatacom.com.br:8080/mge/login.jsp")

driver.implicitly_wait(20)

input_user = driver.find_element(By.CLASS_NAME, "account-inputText")
input_user.send_keys("GUI.MOREIR")

sleep(10)