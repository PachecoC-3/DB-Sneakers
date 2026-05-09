const fetch = require('node-fetch');

const query = `{
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
}`;

fetch('https://db-sneakers-hype-hub-llc.myshopify.com/api/2024-01/graphql.json', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-Shopify-Storefront-Access-Token': '33f66e06740a2a5c1fdfe9fecf9b6a58'
  },
  body: JSON.stringify({ query })
})
.then(res => res.json())
.then(json => console.log(JSON.stringify(json, null, 2)))
.catch(err => console.error(err));
