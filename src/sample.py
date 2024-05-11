import time
from selenium import webdriver

# win環境："Chrome()"内にlocalにあるchromedriverのpathを記載
# mac環境：空のままでOK
driver = webdriver.Chrome()

driver.get('https://www.google.com/')
time.sleep(5)
driver.close()