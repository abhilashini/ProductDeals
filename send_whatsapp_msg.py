import requests


API_ENDPOINT = "https://api.callmebot.com/whatsapp.php?"
API_KEYS = {"+919035377491": "580445"}
# https://api.callmebot.com/whatsapp.php?phone=+919035377491&text=This+is+a+test+from+CallMeBot&apikey=580445

# def send_message(phone_number_with_country_code: str) -> bool:
# 	# params = {
# 	# 	"phone": phone_number_with_country_code,
# 	# 	"text": "Hi!\nTest+message+from+Python",
# 	# 	"apikey": API_KEYS[phone_number_with_country_code]
# 	# }
# 	url = API_ENDPOINT + "phone=" + phone_number_with_country_code + "&text=" + "Hi\nThis+is+a+test+message+from+Python" + "&apikey=" + API_KEYS[phone_number_with_country_code]
# 	api_resp = requests.get(url=url)
	
# 	if not api_resp.text:
# 		print("ERROR: Please check you entered the correct phone number")
# 		return False
# 	return True

def send_message(phone_number, content):
	url = API_ENDPOINT + "phone=" + phone_number + "&text=" + content + "&apikey=" + API_KEYS[phone_number]
	api_resp = requests.get(url=url)
	return api_resp.text

# if send_message("+919035377491"):
# 	print("SUCCESS: WhatsApp Message will be send shortly")