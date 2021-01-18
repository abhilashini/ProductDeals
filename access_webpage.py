import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebsiteSetup():
	def __init__(self, url):
		firefoxOptions = webdriver.FirefoxOptions()
		firefoxOptions.set_headless()
		self.driver = webdriver.Firefox(firefox_options=firefoxOptions)
		self.driver.get(url)

	def set_pincode(self, pincode):
		wait = WebDriverWait(self.driver, 120)
		pincode_span = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/ul/li[1]/div[1]/span/span')))
		pincode_span.click()
		pincode_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rel_pincode"]')))
		pincode_field.send_keys(pincode)
		self.driver.get_screenshot_as_file("pincode_entered.png")
		apply_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/ul/li[1]/div[3]/div[2]/div[3]/div[2]/form/div[1]/button[2]')))
		apply_btn.click()

	def scroll_to_page_end(self):
		prev_height = self.driver.execute_script("return document.body.scrollHeight")
		while True:
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			curr_height = self.driver.execute_script("return document.body.scrollHeight")
			if curr_height == prev_height:
				break
			prev_height = curr_height

	def goto_deals_page(self):
		wait = WebDriverWait(self.driver, 60)
		discount_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/div[4]/div[1]/div[2]/div/div/button[4]')))
		discount_btn.click()
		in_stock_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li/div/div/div/label/input')))
		in_stock_checkbox.click()
		self.scroll_to_page_end()
		return self.driver.execute_script("return document.body.innerHTML")

	def quit_driver(self):
		self.driver.quit()