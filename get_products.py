import requests
from bs4 import BeautifulSoup


def get_discounted_products(endpoint: str, min_discount_pct: int, not_required=None) -> list:
	products_on_discount = []
	products_listing_response = requests.get(url=endpoint)
	soup = BeautifulSoup(products_listing_response.text, 'html.parser')
	all_products = soup.find_all(class_="cat-item")
	for product in all_products:
		# print(f"Current product is ---- {product}")
		discount_pct = product.select(selector=".dis_section span")[0].text
		discount_pct = int(discount_pct.split("%")[0])
		# print(f"Discount Percentage is {discount_pct}\nmin_discount_pct is {min_discount_pct}")
		if discount_pct > min_discount_pct:
			# print()
			# print(f"Discount: {discount_pct}%")
			# print(f"Original Price: {}")
			# print(f"Final Price: {product.find(id='final_price').text}")
			# print()
			product_info = {
				"product_name": product.find(class_="clsgetname").text,
				"discount_pct": f"{discount_pct}",
				"actual_price": product.find(id='price').text,
				"final_price": product.find(id='final_price').text,
			}
			# print(f"Current product_info = \n{product_info}")
			products_on_discount.append(product_info)
	return products_on_discount