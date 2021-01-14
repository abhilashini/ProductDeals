import pprint
import traceback
import time

from progress.bar import Bar

from access_webpage import WebsiteSetup
from send_whatsapp_msg import send_message
from get_products import get_discounted_products


ENDPOINT = "https://www.jiomart.com/c/groceries/2"
REQUIRED_PINCODE = "560076"
NOT_REQUIRED_LIST = ["good life", "perfume", "spray", "cologne", "pencil box"]
MIN_DISCOUNT_PCT = 55
PHONE = "+919035377491"

pp = pprint.PrettyPrinter(indent=4)

try:
	website = WebsiteSetup(REQUIRED_PINCODE)		
	products_on_discount = get_discounted_products(website.page_content, MIN_DISCOUNT_PCT)
	pp.pprint(products_on_discount)
except Exception as e:
	pp.pprint(e)
	pp.pprint(traceback.format_exc())
	print("ERROR! An Exception Occured")
	pass
finally:
	website.quit_driver()