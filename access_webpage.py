import time

from selenium import webdriver


class WebsiteSetup():
	def __init__(self, pincode, url):
		self.driver = webdriver.Firefox()
		self.driver.get(url)
		time.sleep(40)
		print("Fetched URL")
		self.set_pincode(pincode)
		print("Set pincode")
		self.page_content = self.goto_deals_page()

	def set_pincode(self, pincode):
		time.sleep(40)
		print("Slept for 40 in set_pincode before clicking default pincode span")
		self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/ul/li[1]/div[1]/span/span').click()
		print("Clicked default pincode span")
		time.sleep(40)
		# Send required pincode to page
		self.driver.find_element_by_xpath('//*[@id="rel_pincode"]').send_keys(pincode)
		# Click on apply button to select required pincode
		self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/ul/li[1]/div[3]/div[2]/div[3]/div[2]/form/div[1]/button[2]').click()

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
		time.sleep(30)
		self.driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[4]/div[1]/div[2]/div/div/button[4]').click()
		time.sleep(30)
		self.driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li/div/div/div/label/input').click()
		self.scroll_to_page_end()
		return self.driver.execute_script("return document.body.innerHTML")

	def quit_driver(self):
		self.driver.quit()