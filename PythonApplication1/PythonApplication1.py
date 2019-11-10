from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib
from selenium.webdriver.common.keys import Keys
import time
#user_name = "100156819901"
#password = "Champ@2018"
options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)

#driver = webdriver.Chrome()
#driver.maximize_window()
driver.get("https://unifiedportal-mem.epfindia.gov.in/memberinterface/")

string_path = "D:\\Captcha\\Captcha"
i = 10313
while i < 20001:
	string_path1 = string_path + str(i) + ".png"
	with open(string_path1, 'wb') as file:
		file.write(driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div/form/div[4]/div[1]/div/img").screenshot_as_png)
		driver.refresh();
		i += 1
driver.close()

#element = driver.find_element_by_id("userName")
#element.send_keys(user_name)
#element = driver.find_element_by_id("password")
#element.send_keys(password)
#time.sleep(10)
#element = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div/form/div[5]/div[2]/button")
#element.click()
#time.sleep(1)
#element = driver.find_element_by_id("btnCloseModal")
#element.click()
#time.sleep(3)
#element.close()
