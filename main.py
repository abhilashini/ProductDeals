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
# BOLD_START = "\033[1m"
# BOLD_END = "\033[0m"
BOLD_START = BOLD_END = "*"

pp = pprint.PrettyPrinter(indent=4)

# send_message(PHONE, f"{BOLD_START}BOLD+TEST{BOLD_END}\nTab+Test")

def prettify(products, BOLD_START="\033[1m", BOLD_END="\033[0m"):
	for product in products:
		print(f'{BOLD_START}{product["product_name"]}{BOLD_END}')
		print(f'\tDiscount: {product["discount_pct"]}')
		print(f'\tActual Price{product["actual_price"]}\tFinal Price{product["final_price"]}')
		# print(f"\t{}")

def messagify(products):
	all_products = ""
	for product in products:
		all_products += f'{BOLD_START}{product["product_name"]}{BOLD_END}\n'
		all_products += f'Discount: {product["discount_pct"]}\n'
		all_products += f'Actual Price{product["actual_price"]}\n'
		all_products += f'Final Price{product["final_price"]}\n'
	content_ready = all_products.replace(" ", "+")
	return content_ready

try:
	website = WebsiteSetup(REQUIRED_PINCODE, ENDPOINT)		
	products_on_discount = get_discounted_products(website.page_content, MIN_DISCOUNT_PCT)
	prettify(products_on_discount)
	# content = messagify(products_on_discount)
	# send_message(PHONE, content)
except Exception as e:
	pp.pprint(e)
	pp.pprint(traceback.format_exc())
	print("ERROR! An Exception Occured")
finally:
	website.quit_driver()