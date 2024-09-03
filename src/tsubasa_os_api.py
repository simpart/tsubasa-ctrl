from route import flask_app

#app = Flask(__name__)
SERV_PATH = '/var/www/html/tsubasa-os-api'

if __name__ == "__main__":
    flask_app.run(
        ssl_context=(SERV_PATH + '/key/server.crt', SERV_PATH + '/key/server.key'),
        debug=True,
        port=8080,
        host="0.0.0.0"
    )
