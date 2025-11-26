import requests
# url = "https://jsonplaceholder.typicode.com/users"
url = "https://mern-backend-drab-rho.vercel.app/api/products/6925cb229ec5211c57699755"
# requests.delete(url)

data = {
    "productName": "Product Fig"
    }

requests.patch(url,json=data)
# res = requests.get(url).json()
# print(res['products'])
# for i in res["products"]:
#     print(i["productName"])
data = {
    "productName": "Product F",
    "description": "This is description",
    "price": 100,
    "imgUrl": "https://picsum.photos/id/10/300/300"
    }
# response = requests.post(url, json=data)
# print("Status Code:", response.status_code)
# print("Response:", response.json())
# requests.post(url,json=data)