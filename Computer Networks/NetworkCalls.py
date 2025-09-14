import requests

print("Namaskara")

r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status:", r.status_code)
print("Headers:", r.headers)
print("Body:", r.text[:120], "...")