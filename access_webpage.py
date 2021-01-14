import time

from selenium import webdriver


class WebsiteSetup():
	def __init__(self, pincode):
		self.driver = webdriver.Firefox()
		self.driver.get("https://www.jiomart.com")
		self.set_pincode(pincode)
		self.page_content = self.goto_deals_page()
		# self.scroll_till_page_end()
		print("SUCCESS: Product deals page ready to use")

	def set_pincode(self, pincode):
		self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/ul/li[1]/div[1]/span/span").click()
		# Send required pincode to page
		self.driver.find_element_by_xpath('//*[@id="rel_pincode"]').send_keys(pincode)
		# Click on apply button to select required pincode
		self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/ul/li[1]/div[3]/div[2]/div[3]/div[2]/form/div[1]/button[2]').click()
		print("SUCCESS: Required pincode set")

	def goto_deals_page(self):
		self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[3]/h1/a').click()
		# Sort products by discount
		self.driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/div[4]/div[1]/div[2]/div/div/button[4]').click()
		# Select only products in stock
		self.driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li/div/div/div/label/input').click()
		print("SUCCESS: Sorted products by discount and selected products in stock")
		self.scroll_till_page_end()
		return self.driver.execute_script("return document.body.innerHTML")

	def scroll_till_page_end(self):
		prev_height = self.driver.execute_script("return document.body.scrollHeight")
		while True:
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			curr_height = self.driver.execute_script("return document.body.scrollHeight")
			if curr_height == prev_height:
				break
			prev_height = curr_height

	def quit_driver(self):
		self.driver.quit()
		print("SUCCESS: Web Driver Quit")