## URL Shortener
### Acknowledgements
> [!WARNING]
> A service for managing your redirects (Creating, deleting, editing, etc) is not included, however all you need to do is edit the objects in mongo for which you can use your own script or mongodb compass.

> [!NOTE]
> This server is built for tight integration with https://alecks.dev and other services running there, hense why it uses MongoDB and not something local such as SQLite

## Creating Redirects
Make a database named url_shortener and a collection inside of it named redirects. In the redirects collection create an object with an id value and link value which is where you'll be redirected to.

Using pymongo (This creates a redirect at /example, which takes you to https://example.com)
``client.url_shortener.redirects.insert_one({"id": "example","link": "https://example.com"})``

## Deployment Options
Depending on your needs, you're able to deploy the server either in a standalone container (behind your own reverse proxy), or with my docker compose preset which provides an all-in-one solution.

### Standalone Setup
> [!NOTE]
> You'll have to source your own database connection string as the docker image only includes a web server. (The string used below is a placeholder)

```
docker run -d --name=url-shortener-web --restart=unless-stopped -p 80:80 -e MONGO_URL="mongodb://mongo" ghcr.io/alecks20/url-shortener:latest
```
This creates a container named url-shortener-web and exposes it to port 80, make sure you change the MONGO_URL variable
### Compose Setup (All-in-one)
> [!NOTE]
> This includes a MongoDB database which is already configured for use and a Caddy reverse proxy

```
git clone https://github.com/alecks20/url-shortener
cd url-shortener
```
Change the HOSTNAME variable to whatever url your server will be publically available (In compose.yml, line 25)
```
nano compose.yml
```
After that you should be good to start it up
```
docker compose up -d
```

