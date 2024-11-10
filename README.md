## Creating redirects
Make a database named url_shortener and a collection inside of it named redirects. In the redirects collection create an object with an id value and link value which is where you'll be redirected to.

Using pymongo (Likely integrating with some other service)
``client.url_shortener.redirects.insert_one({"id": "example","link": "https://example.com"})``
