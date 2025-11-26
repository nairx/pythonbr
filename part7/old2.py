import requests
url = "https://jsonplaceholder.typicode.com/users/"
url = "https://mern-backend-drab-rho.vercel.app/api/products/6925cb229ec5211c57699755"
res = requests.get(url).json()
res = requests.delete(url)
data = {
    "productName": "Product F",
    "description": "This is description",
    "price": 100,
    "imgUrl": "https://picsum.photos/id/10/300/300"
    }
res = requests.post(url, json=data)
Res = requests.patch(url,json=data)
for i in res: #res["products"]
     print(i)
      #print(i[name])
