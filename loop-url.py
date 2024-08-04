import requests

url = "https://sophalalin.tutor93.com"  # Replace with the IP address or domain of your Nginx server
iterations = 200  # Number of requests to send

for i in range(iterations):
    response = requests.get(url)
    print(f"Response {i + 1}: {response.status_code} from {response.url} in {response.elapsed.total_seconds()}s")