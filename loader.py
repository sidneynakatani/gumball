from flask import Flask, request, jsonify, redirect
from util.balancer import Balancer

app = Flask(__name__)


@app.route('/')
def home():
    b1 = Balancer()
    print b1.host_selector()

    b1.change_host()

    b2 = Balancer()
    print b2.host_selector()

    return 'Hello!'


if __name__ == '__main__':
    app.run(debug=True)
