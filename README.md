## URL Shortener
### Acknowledgements
> [!WARNING]
> A service for managing your redirects (Creating, deleting, editing, etc) is not included as on the production instance it's done via my api server which is currently closed-source (subject to change, but It'll be a while)

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
cp .env.example .env
nano .env
```
After that you should be good to start it up
```
docker compose up -d
```

