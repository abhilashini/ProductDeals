import argparse
import math
import os
import pprint
import time
import traceback

from progress.bar import Bar

from access_webpage import WebsiteSetup
from send_whatsapp_msg import send_message
from get_products import get_discounted_products as disounted_products


ENDPOINT = "https://www.jiomart.com/c/groceries/2"
REQUIRED_PINCODE = "560076"
NOT_REQUIRED_LIST = ["good life", "perfume", "spray", "cologne", "pencil box", "chicken", "fish", "mutton", "agarbatti"]
MIN_DISCOUNT_PCT = 40
PHONE = "+919035377491"
BOLD_START = "\033[1m"
BOLD_END = "\033[0m"
BOLD_START = BOLD_END = "*"
ITALIC_START = "\x1B[3m"
ITALIC_END = "\x1B[23m"


def prettify(products, BOLD_START="\033[1m", BOLD_END="\033[0m"):
	for product in products:
		print(f'{BOLD_START}{product["product_name"]}{BOLD_END}')
		print(f'\tDiscount: {product["discount_pct"]}')
		print(f'\tActual Price{product["actual_price"]}\tFinal Price{product["final_price"]}')
		# print(f"\t{}")

def fileify(products, file=None):
	all_products = ""
	for product in products:
		all_products += f'{product["product_name"]}\n'
		all_products += f'\tDiscount: {product["discount_pct"]}\n'
		all_products += f'\tActual Price{product["actual_price"]}\tFinal Price{product["final_price"]}'
		all_products += '\n\n'

	if not file:
		file = "discounted_products.txt"
		path = os.getcwd()
	else:
		path = os.path.dirname(file)

	with open(file, 'w') as f:
		f.write(all_products)

	print(f"\nCOMPLETE: Discounted products listing can be found at: \n\t{path}")

def messagify(products):
	all_products = ""
	for product in products:
		all_products += f'{BOLD_START}{product["product_name"]}{BOLD_END}\n'
		all_products += f'Discount: {product["discount_pct"]}\n'
		all_products += f'Actual Price{product["actual_price"]}\n'
		all_products += f'Final Price{product["final_price"]}\n'
	content_ready = all_products.replace(" ", "+")
	return content_ready

parser = argparse.ArgumentParser(description=f"Get Top Discounted Products from {ITALIC_START}jiomart.com{ITALIC_END}")
parser.add_argument('--percent', '--pct', type=str, help="Minimum discount percent you're looking for", required=True)
parser.add_argument('--pincode', type=str, help="Pincode of area you are in")
parser.add_argument('--loc', type=str, help="Location with file name of text file where you want discounted products listing to be saved in")
args = parser.parse_args()

if args.pincode:
	REQUIRED_PINCODE = args.pincode

if "%" in args.percent:
	discount_pct = int(math.floor(args.percent.split("%")[0]))
else:
	discount_pct = int(args.percent)

pp = pprint.PrettyPrinter(indent=4)

try:
	website = WebsiteSetup(ENDPOINT)
	start = time.time()
	website.set_pincode(REQUIRED_PINCODE)
	end = time.time()
	print(f"Time taken to set pincode = {round((end-start), 2)} seconds\n")

	start = time.time()
	page_content = website.goto_deals_page()
	end = time.time()
	print(f"Time taken to completely load deals page = {round((end-start), 2)} seconds\n")

	start = time.time()
	products_on_discount = disounted_products(page_content, discount_pct, NOT_REQUIRED_LIST)
	end = time.time()
	print(f"Time taken to write products listing = {round(end-start, 2)} seconds\n")
	
	print(f"These products aren't included in the listing —")
	for prd in NOT_REQUIRED_LIST:
		print(f"\t{prd.title()}")

	fileify(products_on_discount, args.loc)
except Exception as e:
	print("ERROR! An Exception Occured")
	pp.pprint(e)
	# pp.pprint(traceback.format_exc())
finally:
	website.quit_driver()