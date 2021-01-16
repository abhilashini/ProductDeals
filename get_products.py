from bs4 import BeautifulSoup


def get_discounted_products(page_content: str, min_discount_pct: int, not_required=None) -> list:
	products_on_discount = []
	soup = BeautifulSoup(''.join(page_content), 'html.parser')
	all_products = soup.find_all(class_="cat-item")
	# print(len(all_products), "<----- this is how many products I found")
	for product in all_products:
		discount_pct = product.select(selector=".dis_section span")[0].text
		discount_pct = int(discount_pct.split("%")[0])
		if discount_pct > min_discount_pct:
			product_info = {
				"product_name": product.find(class_="clsgetname").text,
				"discount_pct": f"{discount_pct}%",
				"actual_price": product.find(id='price').text,
				"final_price": product.find(id='final_price').text,
			}
			products_on_discount.append(product_info)
	return products_on_discount