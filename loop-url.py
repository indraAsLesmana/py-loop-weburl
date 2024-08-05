import requests # pip install requests

url = "http://192.168.2.31:1080" # nginx ip or domain
iterations = 200  # Number of requests to send

for i in range(iterations):
    response = requests.get(url)
    print(f"Response {i + 1}: {response.status_code} from {response.url} in {response.elapsed.total_seconds()}s")