import requests
url = "https://mern-backend-drab-rho.vercel.app/api/products/6925cb229ec5211c57699755"
# res = requests.get(url).json()
# for i in res["products"]:
#     print(i["productName"],i["description"])
# data = {
#         "productName": "Product 1",
#         "description": "This is description",
#         "price": 500,
#         "imgUrl": "https://picsum.photos/id/10/300/300",
#   }
# res = requests.post(url,json=data)
# res = requests.delete(url)

data = {
    "productName":"iPhone"
}
res = requests.patch(url,json=data)


