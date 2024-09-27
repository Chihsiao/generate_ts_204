# Tailscale Captive Portal Detection Endpoint

generate_ts_204 is a simple web application designed to act as a Tailscale captive portal detection endpoint. It is intended to be used with Tailscale's network connectivity checks to help identify when a device is behind a captive portal. The application responds to HTTP requests at the `/generate_204` endpoint with a `204 No Content` status code and a specific `X-Tailscale-Response` header, which Tailscale uses to determine the presence of a captive portal.

## Features

- Responds to HTTP GET requests at `/generate_204` with a `204 No Content` status.
- Sets the `X-Tailscale-Response` header with the value `ts_<hostname>` where `<hostname>` is the hostname of the server.
- Can be deployed behind a reverse proxy for production use.

## Requirements

- Python 3.12 (or higher)
- Flask (for serving the web application)
- Waitress (as a production-ready WSGI server)

## Installation

### Docker

The easiest way to deploy this application is via Docker. Ensure you have Docker installed on your system, then follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/Chihsiao/generate_ts_204.git
   cd generate_ts_204
   ```

2. Build the Docker image:
   ```bash
   docker build -t generate-ts-204 .
   ```

3. Run the Docker container:
   ```bash
   docker run -d --name generate_ts_204 -p 8080:8080 generate-ts-204
   ```

The application will now be running and accessible at `http://localhost:8080/generate_204`.

### Without Docker

If you prefer not to use Docker, you can install the dependencies and run the application locally:

1. Clone this repository and navigate to it:
   ```bash
   git clone https://github.com/Chihsiao/generate_ts_204.git
   cd generate_ts_204
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:
   ```bash
   waitress-serve app:app
   ```

The application will now be running and accessible at `http://localhost:8080/generate_204`.

## Configuration with Reverse Proxy

It is designed to work behind a reverse proxy such as Nginx or Apache.

Here is an example Nginx configuration to reverse proxy requests to the `generate_ts_204` application:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location /generate_204 {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
