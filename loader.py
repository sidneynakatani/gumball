from flask import Flask, request, jsonify, redirect
from util.balancer import Balancer


app = Flask(__name__)
b1 = Balancer()

@app.route('/')
def home():
    
    host =  b1.host_selector()
    b1.change_host()
    return redirect(host, 301) 


if __name__ == '__main__':
    app.run(debug=True)
