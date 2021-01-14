from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = None

def set_driver():
	global driver
	driver = webdriver.Firefox()
	# driver.get("https://www.jiomart.com/") # Get webpage
	driver.get("https://www.jiomart.com/c/groceries/2")

def set_pincode(pincode):
	global driver
	##### SET PINCODE #####
	# Find <span> containing default pincode
	driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/ul/li[1]/div[1]/span/span").click()
	# Send required pincode to page
	driver.find_element_by_xpath('//*[@id="rel_pincode"]').send_keys(pincode)
	# Click on apply button to select required pincode
	driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/ul/li[1]/div[3]/div[2]/div[3]/div[2]/form/div[1]/button[2]').click()

def sort_by_discount():
	global driver
	# if driver.find_element_by_css_selector(".overlay_bg"):
	# 	driver.find_element_by_css_selector(".overlay_bg").click()
	driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[4]/div[1]/div[2]/div/div/button[4]').click()
	driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li/div/div/div/label/input').click()

def goto_deals_page():
	##### GO TO TOP DEALS PAGE #####
	WebDriverWait(driver, 60).until(EC.element_to_be_clickable(By.XPATH, '/html/body/div[1]/div[4]/section[3]/h1/a')).click()
	# driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[3]/h1/a').click()
	# Sort products by discount
	WebDriverWait(driver, 120).until(EC.element_to_be_clickable(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/div[4]/div[1]/div[2]/div/div/button[4]')).click()
	# driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[4]/div[1]/div[2]/div/div/button[4]').click()
	# Select only InStock products
	driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li/div/div/div/label/input').click()
	return driver.current_url

def quit_driver():
	driver.quit()