import urllib.request
import json

url = 'https://db-sneakers-hype-hub-llc.myshopify.com/api/2024-01/graphql.json'
query = """{
  products(first: 250, query: "title:*VALENTINE*") {
    edges {
      node {
        title
        variants(first: 5) {
          edges {
            node {
              price { amount }
              compareAtPrice { amount }
            }
          }
        }
      }
    }
  }
}"""

req = urllib.request.Request(url, data=json.dumps({'query': query}).encode('utf-8'))
req.add_header('Content-Type', 'application/json')
req.add_header('X-Shopify-Storefront-Access-Token', '33f66e06740a2a5c1fdfe9fecf9b6a58')

try:
    response = urllib.request.urlopen(req)
    print(json.dumps(json.loads(response.read()), indent=2))
except Exception as e:
    print(e)
