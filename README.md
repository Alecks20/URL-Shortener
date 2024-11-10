## Creating redirects
Make a database named url_shortener and a collection inside of it named redirects. In the redirects collection create an object with an id value and link value which is where you'll be redirected to.

Using pymongo (This creates a redirect at /example, which takes you to https://example.com)
``client.url_shortener.redirects.insert_one({"id": "example","link": "https://example.com"})``
