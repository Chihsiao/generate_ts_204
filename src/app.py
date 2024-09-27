from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/generate_204')
def __api_generate_ts_204():
    response = make_response()
    hostname, _, port = request.host.partition(':')
    response.headers['X-Tailscale-Response'] = f'response ts_{hostname}'
    response.status_code = 204
    return response


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
