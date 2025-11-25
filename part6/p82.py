import requests
url = "https://jsonplaceholder.typicode.com/users"
res = requests.get(url).json()
print(res)
# for i in res:
#     print(i["name"],i["email"])