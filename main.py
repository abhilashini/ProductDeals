from access_webpage import set_driver, set_pincode, sort_by_discount, quit_driver
from send_whatsapp_msg import send_message
from get_products import get_discounted_products


ENDPOINT = "https://www.jiomart.com/c/groceries/2"
REQUIRED_PINCODE = "560076"
NOT_REQUIRED_LIST = ["good life", "perfume", "spray", "cologne", "pencil box"]
MIN_DISCOUNT_PCT = 5
PHONE = "+919035377491"

try:
	set_driver()
	print("Web Driver Ready")
	set_pincode(REQUIRED_PINCODE)
	print("Changed to required pincode")
	# deals_endpoint = goto_deals_page().split("?")[0]
	# print("Entered deals page")
	# print(f"deals_endpoint = {deals_endpoint}")
	sort_by_discount()
	print("Sorted products by discount percentage")
	products_on_discount = get_discounted_products(ENDPOINT, MIN_DISCOUNT_PCT)
	print(products_on_discount)
except Exception as e:
	print(e)
	print("ERROR! An Exception Occured")
	pass
finally:
	quit_driver()