import requests, json

def get_token():
	api_path = "https://sandboxdnac.cisco.com/dna"
	auth = ("devnetuser", "Cisco123!")
	headers = {"Content-Type":  "application/json"}

	auth_resp = requests.post(f"{api_path}/system/api/v1/auth/token", auth = auth, headers = headers)

	auth_resp.raise_for_status()
	#print(auth_resp)
	token = auth_resp.json()["Token"]
	return token

def get_device(token):
	headers = {"Content-Type": "application/json", "X-Auth-Token": token }
	api_path = "https://sandboxdnac.cisco.com/dna"
	auth_resp1 = requests.get(f"{api_path}/intent/api/v1/network-device", headers = headers)
	return auth_resp1

def main():
	token = get_token()
	for device in get_device(token).json()["response"]:
		print(device['id'], device["managementIpAddress"])

if __name__ == "__main__":
	main()


	

