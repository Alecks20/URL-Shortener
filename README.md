## Creating redirects
On your mongodb instance make a database called url_shortener, then make a collection inside of it called redirects. In the redirects collection each object is a different redirect, so to make a redirect create an object with an id value (What will be after the /), and a link value which is where you'll be redirected to.

Using pymongo (Probably integrating with some api or something)
``client.url_shortener.redirects.insert_one({"id": "example","link": "https://example.com"})``
